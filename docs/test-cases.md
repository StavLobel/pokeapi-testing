# PokéAPI v2 – User-Story Test Cases (Grouped by Resource Family)

> Format: each test is a user story with a unique ID.  
> Scope: Pokémon, Abilities, Moves, Types, Items, Berries, Machines, Evolution, Encounters, Games (Version Groups), Locations, Regions, Pokedexes, Generations, Versions.  
> Notes:
> - PokéAPI is read-only (GET only). No auth. Default list pagination uses `limit`/`offset` (default page size is 20).  
> - Where docs are ambiguous (e.g., behavior for invalid query params), tests define a conservative stance: expect a clear client error (preferably 400) or a consistent, safe defaulting behavior. Capture actual behavior and baseline it.

---

## Pokémon

- **POK-01**: *As an API consumer, I want to retrieve a Pokémon by a valid ID so that I receive **200 OK** with the correct Pokémon details (happy path by ID).*  
- **POK-02**: *As an API consumer, I want to retrieve a Pokémon by a valid name so that I get **200 OK** with that Pokémon’s JSON (happy path by name).*  
- **POK-03**: *As an API consumer, I want to list Pokémon with no query params so that I receive a default page (about 20) with `count`, `next`, `previous`, and `results` (happy path listing).*  
- **POK-04**: *As an API consumer, I want to list Pokémon with `limit`/`offset` so that I can page through results and see correct `next`/`previous` links (pagination behavior).*  
- **POK-05**: *As an API consumer, I want boundary pagination on Pokémon (limit=0/1/high; offset=0/end/beyond) so that the API returns empty or partial pages consistently without error.*  
- **POK-06**: *As an API consumer, I want the Pokémon schema to match docs (required fields, types, nesting: abilities, moves, types, stats, sprites, species) so that responses are structurally correct (schema validation).*  
- **POK-07**: *As an API consumer, I want nested references in Pokémon (e.g., abilities, types, moves) to be valid named resources so that cross-links are navigable (schema & nesting).*  
- **POK-08**: *As an API consumer, I want **404 Not Found** when I request a non-existent Pokémon by ID or name so that invalid lookups are handled.*  
- **POK-09**: *As an API consumer, I want a clear outcome for invalid `limit`/`offset` (non-numeric, negative, out-of-range) so that malformed queries return a client error (prefer 400) or a documented safe default (ambiguity acknowledged).*  
- **POK-10**: *As an API consumer, I want non-GET methods on Pokémon to return **405 Method Not Allowed** so that the read-only contract is enforced.*  
- **POK-11**: *As an API consumer, I want server faults on Pokémon to return **5xx** without internal details so that server errors are clear and contained.*  
- **POK-12**: *As an API consumer, I want cross-resource consistency (e.g., Pokémon with ability X appears in ability X’s `pokemon` list; Pokémon of type T appears in type T’s `pokemon` entries) so that bidirectional links are correct.*

---

## Abilities

- **ABL-01**: *Retrieve an Ability by valid ID → **200 OK** with full details (id, name, is_main_series, generation, effect/flavor text, `pokemon`).*  
- **ABL-02**: *Retrieve an Ability by valid name → **200 OK** with same data as ID.*  
- **ABL-03**: *List Abilities (no params) → default paginated list with `count`/`next`/`previous`/`results`.*  
- **ABL-04**: *Paginate Abilities with `limit`/`offset` → correct page lengths and links.*  
- **ABL-05**: *Ability schema correctness (required fields, localized texts, generation, `pokemon` list entries with `is_hidden`, `slot`).*  
- **ABL-06**: *Non-existent Ability id/name → **404 Not Found**.*  
- **ABL-07**: *Invalid pagination inputs on Ability list → client error (prefer **400**) or consistent default (ambiguity acknowledged).*  
- **ABL-08**: *Non-GET on `/ability` or `/ability/{id|name}` → **405 Method Not Allowed**.*  
- **ABL-09**: *Server error while fetching an Ability → **5xx** with generic error.*  
- **ABL-10**: *Cross-resource: Ability’s `pokemon` includes a species that also lists the ability in the species/Pokémon data; generation linkage consistent with Generation resource.*

---

## Moves

- **MOV-01**: *Retrieve a Move by valid ID → **200 OK** with accuracy/power/pp/type/damage_class/effect entries/etc.*  
- **MOV-02**: *Retrieve a Move by valid name → **200 OK** with same details as ID.*  
- **MOV-03**: *List Moves (no params) → default paginated list with `count`/`next`/`previous`.*  
- **MOV-04**: *Paginate Moves with `limit`/`offset` → correct lengths and links, boundary checks.*  
- **MOV-05**: *Move schema correctness (required fields; null handling for accuracy/power where applicable; `learned_by_pokemon`; `machines`; localizations).*  
- **MOV-06**: *Non-existent Move id/name → **404 Not Found**.*  
- **MOV-07**: *Invalid pagination inputs on Move list → client error (prefer **400**) or consistent default (ambiguity acknowledged).*  
- **MOV-08**: *Non-GET on Move endpoints → **405 Method Not Allowed**.*  
- **MOV-09**: *Server error on Move retrieval → **5xx**.*  
- **MOV-10**: *Cross-resource: Move’s `type` matches `/type/{name}`; move appears under that type’s `moves`; Pokémon listed in `learned_by_pokemon` show the move within their learnsets; machine references align with `/machine` and `/item`.*

---

## Types

- **TYP-01**: *Retrieve a Type by valid ID → **200 OK** with damage relations, game indices, generation, move damage class, `pokemon`, `moves`.*  
- **TYP-02**: *Retrieve a Type by valid name → **200 OK** with same details as ID.*  
- **TYP-03**: *List Types (no params) → (likely full set in one page) with `count`/`results`.*  
- **TYP-04**: *Paginate Types with `limit`/`offset` → parameters honored; links valid (even if list is small).*  
- **TYP-05**: *Type schema correctness: `damage_relations` (double/half/no damage to/from); `past_damage_relations`; `pokemon` entries (with `slot`); `moves` list.*  
- **TYP-06**: *Non-existent Type id/name → **404 Not Found** (case-sensitive names).*  
- **TYP-07**: *Invalid pagination inputs on Type list → client error (prefer **400**) or consistent default.*  
- **TYP-08**: *Non-GET on Type endpoints → **405 Method Not Allowed**.*  
- **TYP-09**: *Server error on Type retrieval → **5xx**.*  
- **TYP-10**: *Cross-resource: If Fire lists double_damage_to Grass, Grass lists double_damage_from Fire; Pokémon and Moves listed under Type are consistent with their own `types`/`type` fields.*

---

## Items

- **ITM-01**: *Retrieve an Item by valid ID → **200 OK** with cost/category/attributes/effects/flavor text/sprites/held_by.*  
- **ITM-02**: *Retrieve an Item by valid name → **200 OK** with same details as ID.*  
- **ITM-03**: *List Items (no params) → default paginated list with `count` and `results`.*  
- **ITM-04**: *Paginate Items with `limit`/`offset` → correct lengths and links; offset at end returns empty list.*  
- **ITM-05**: *Item schema correctness: `attributes` (named refs), `category` (named ref), `effect_entries`, `flavor_text_entries`, `game_indices`, `sprites`, `held_by_pokemon`, `baby_trigger_for` (nullable).*  
- **ITM-06**: *Non-existent Item id/name → **404 Not Found** (case-sensitive, hyphenated names).*  
- **ITM-07**: *Invalid pagination inputs on Item list → client error (prefer **400**) or consistent default.*  
- **ITM-08**: *Non-GET on Item endpoints → **405 Method Not Allowed**.*  
- **ITM-09**: *Server error on Item retrieval → **5xx**.*  
- **ITM-10**: *Cross-resource: Item’s `category` contains the item; item attributes list the item; if item is a TM/HM, `/machine` and `/move` references align; `held_by_pokemon` reconcile with Pokémon `held_items`.*

---

## Berries (and sub-resources: Firmness, Flavor)

- **BER-01**: *Retrieve a Berry by valid ID → **200 OK** with growth_time/max_harvest/natural_gift/type/firmness/flavors/item.*  
- **BER-02**: *Retrieve a Berry by valid name → **200 OK** with same details as ID.*  
- **BER-03**: *List Berries (no params) → default paginated list with `count` and `results`.*  
- **BER-04**: *Paginate Berries with `limit`/`offset` → boundaries honored; links correct.*  
- **BER-05**: *Berry schema correctness: `firmness` (named ref), `flavors[]` (with potency and flavor ref), `item` (named ref), `natural_gift_type`.*  
- **BER-06**: *Retrieve Berry Firmness by ID or name → **200 OK** with list of berries and localized names.*  
- **BER-07**: *List Berry Firmness → full set (likely single page) with correct `count`.*  
- **BER-08**: *Retrieve Berry Flavor by ID or name → **200 OK** with berries (potency) and contest type.*  
- **BER-09**: *List Berry Flavor → full set (likely single page) with correct `count`.*  
- **BER-10**: *Non-existent Berry/Firmness/Flavor → **404 Not Found**.*  
- **BER-11**: *Invalid params on berry lists → client error (prefer **400**) or consistent default.*  
- **BER-12**: *Non-GET on berry endpoints → **405 Method Not Allowed**.*  
- **BER-13**: *Server error on berry endpoints → **5xx**.*  
- **BER-14**: *Cross-resource: Berry’s `firmness` lists the berry; Berry’s flavors appear in `/berry-flavor/{name}` with same potency; Berry’s `item` corresponds to an `/item/{name}` in the Berries category.*

---

## Machines

- **MAC-01**: *Retrieve a Machine by valid ID → **200 OK** with `item`, `move`, `version_group` references.*  
- **MAC-02**: *List Machines (no params) → default paginated list (unnamed resource entries expose only `url`).*  
- **MAC-03**: *Paginate Machines with `limit`/`offset` → correct lengths and navigation.*  
- **MAC-04**: *Machine schema correctness: `id`, `item` (TM/HM item), `move`, `version_group` (all named refs).*  
- **MAC-05**: *Non-existent Machine ID → **404 Not Found**; text keys return 404 (unnamed resource).*  
- **MAC-06**: *Invalid pagination on Machines → client error (prefer **400**) or consistent default.*  
- **MAC-07**: *Non-GET on Machine endpoints → **405 Method Not Allowed**.*  
- **MAC-08**: *Server error on Machine retrieval → **5xx**.*  
- **MAC-09**: *Cross-resource: Machine’s `item` appears as a machine under `/item`; Machine’s `move` references the same move; Version Group aligns with `/version-group`.*

---

## Evolution (Chains and Triggers)

- **EVO-01**: *Retrieve an Evolution Chain by valid ID → **200 OK** with nested `chain` and `evolution_details`.*  
- **EVO-02**: *List Evolution Chains (no params) → default paginated list (unnamed resource, `url` only).*  
- **EVO-03**: *Retrieve an Evolution Trigger by valid ID or name → **200 OK** with `pokemon_species` list.*  
- **EVO-04**: *List Evolution Triggers → all triggers present with `count`.*  
- **EVO-05**: *Evolution Chain schema: `id`, `baby_trigger_item` (nullable), root `chain` with `species`, `evolves_to[]` and `evolution_details` (trigger/item/min_level etc.).*  
- **EVO-06**: *Evolution Trigger schema: `id`, `name`, `names`, `pokemon_species`.*  
- **EVO-07**: *Non-existent chain id or trigger id/name → **404 Not Found**; names invalid for chains (unnamed).*  
- **EVO-08**: *Invalid pagination on chain list → client error (prefer **400**) or consistent default.*  
- **EVO-09**: *Non-GET on Evolution endpoints → **405 Method Not Allowed**.*  
- **EVO-10**: *Server error on Evolution endpoints → **5xx**.*  
- **EVO-11**: *Cross-resource: Species’ evolution info matches Evolution Chain; Trigger’s species set aligns with species that have that trigger; Species’ generation ties in where relevant.*

---

## Encounters (Methods, Conditions, Condition Values)

- **ENC-01**: *Retrieve Encounter Method by valid ID or name → **200 OK** with `order` and `names`.*  
- **ENC-02**: *List Encounter Methods → full set listed (likely single page) with `count`.*  
- **ENC-03**: *Retrieve Encounter Condition by valid ID or name → **200 OK** with `values` and `names`.*  
- **ENC-04**: *List Encounter Conditions → full set listed with `count`.*  
- **ENC-05**: *Retrieve Encounter Condition Value by valid ID or name → **200 OK** with parent `condition` and `names`.*  
- **ENC-06**: *List Encounter Condition Values → full set listed with `count`.*  
- **ENC-07**: *Schema correctness across all three: required fields present; `values` link to condition values; condition value’s `condition` points back.*  
- **ENC-08**: *Non-existent id/name on any encounter endpoint → **404 Not Found**.*  
- **ENC-09**: *Invalid pagination inputs where applicable → client error (prefer **400**) or consistent default.*  
- **ENC-10**: *Non-GET on encounter endpoints → **405 Method Not Allowed**.*  
- **ENC-11**: *Server error on encounter endpoints → **5xx**.*  
- **ENC-12**: *Cross-resource: Location Area encounter details reference valid encounter methods and condition values; references resolve to these endpoints correctly.*

---

## Games (Version Groups)

- **GAM-01**: *Retrieve Version Group by valid ID or name → **200 OK** with `order`, `generation`, `move_learn_methods`, `pokedexes`, `regions`, `versions`.*  
- **GAM-02**: *List Version Groups (no params) → default paginated list with `count`/links.*  
- **GAM-03**: *Paginate Version Groups with `limit`/`offset` → lengths and links correct.*  
- **GAM-04**: *Version Group schema correctness: all lists and named refs present and valid.*  
- **GAM-05**: *Non-existent version-group id/name → **404 Not Found**.*  
- **GAM-06**: *Invalid pagination inputs on Version Group list → client error (prefer **400**) or consistent default.*  
- **GAM-07**: *Non-GET on Version Group endpoints → **405 Method Not Allowed**.*  
- **GAM-08**: *Server error on Version Group retrieval → **5xx**.*  
- **GAM-09**: *Cross-resource: Version Group’s `versions` link back to this group; `regions` reciprocate; `pokedexes` reciprocate; `generation` matches Generation resource.*

---

## Locations (and Location Areas)

- **LOC-01**: *Retrieve Location by valid ID or name → **200 OK** with `region`, `names`, `game_indices`, `areas`.*  
- **LOC-02**: *List Locations (no params) → default paginated list with `count`/links.*  
- **LOC-03**: *Paginate Locations with `limit`/`offset` → correct lengths and links; offset edge returns empty list.*  
- **LOC-04**: *Location schema correctness: `region` (non-null named ref), `areas` (possibly empty array), `game_indices` (with generation refs).*  
- **LOC-05**: *Retrieve Location Area by valid ID or name → **200 OK** with `game_index`, `encounter_method_rates`, `location`, `names`, `pokemon_encounters`.*  
- **LOC-06**: *List Location Areas → paginated list (unnamed; entries may be `url`-only).*  
- **LOC-07**: *Location Area schema correctness: nested `encounter_method_rates` and `pokemon_encounters` structures present and typed correctly.*  
- **LOC-08**: *Non-existent Location/Location Area id/name → **404 Not Found**.*  
- **LOC-09**: *Invalid pagination inputs on Location/Area lists → client error (prefer **400**) or consistent default.*  
- **LOC-10**: *Non-GET on Location endpoints → **405 Method Not Allowed**.*  
- **LOC-11**: *Server error on Location endpoints → **5xx**.*  
- **LOC-12**: *Cross-resource: Location’s `region` reciprocates by listing the location; listed `areas` reciprocate by pointing back to the parent location; encounter references resolve to valid Encounter endpoints.*

---

## Regions

- **REG-01**: *Retrieve Region by valid ID or name → **200 OK** with `locations`, `main_generation`, `names`, `pokedexes`, `version_groups`.*  
- **REG-02**: *List Regions → likely full set in one page with `count`.*  
- **REG-03**: *Paginate Regions with `limit`/`offset` → parameters honored, even if small list.*  
- **REG-04**: *Region schema correctness: required fields present; `locations` and other lists contain valid named refs.*  
- **REG-05**: *Non-existent Region id/name → **404 Not Found**.*  
- **REG-06**: *Invalid pagination inputs on Region list → client error (prefer **400**) or consistent default.*  
- **REG-07**: *Non-GET on Region endpoints → **405 Method Not Allowed**.*  
- **REG-08**: *Server error on Region retrieval → **5xx**.*  
- **REG-09**: *Cross-resource: Region’s `main_generation` points to Generation whose `main_region` is this Region; `pokedexes` and `version_groups` reciprocate; `locations` reciprocate.*

---

## Pokedexes

- **PDX-01**: *Retrieve a Pokédex by valid ID or name → **200 OK** with `is_main_series`, `descriptions`, `names`, `pokemon_entries`, `region` (nullable for National), `version_groups`.*  
- **PDX-02**: *List Pokedexes (no params) → resource list with `count`.*  
- **PDX-03**: *Paginate Pokedexes with `limit`/`offset` → parameters honored.*  
- **PDX-04**: *Pokedex schema correctness: `pokemon_entries` have `entry_number` and `pokemon_species` refs; `region` correct/nullable; localizations present.*  
- **PDX-05**: *Non-existent Pokedex id/name → **404 Not Found**.*  
- **PDX-06**: *Invalid pagination inputs on Pokedex list → client error (prefer **400**) or consistent default.*  
- **PDX-07**: *Non-GET on Pokedex endpoints → **405 Method Not Allowed**.*  
- **PDX-08**: *Server error on Pokedex retrieval → **5xx**.*  
- **PDX-09**: *Cross-resource: Pokedex’s `region` reciprocates; `version_groups` reciprocate; species entries align with species’ pokedex numbering where exposed.*

---

## Generations

- **GEN-01**: *Retrieve a Generation by valid ID or name → **200 OK** with `abilities` (introduced), `main_region`, `moves` (introduced), `names`, `pokemon_species` (introduced), `types` (introduced), `version_groups`.*  
- **GEN-02**: *List Generations (no params) → resource list with `count`.*  
- **GEN-03**: *Paginate Generations with `limit`/`offset` → parameters honored (small list).*  
- **GEN-04**: *Generation schema correctness: all introduced lists and refs present and valid; localizations present.*  
- **GEN-05**: *Non-existent Generation id/name → **404 Not Found**.*  
- **GEN-06**: *Invalid pagination inputs on Generation list → client error (prefer **400**) or consistent default.*  
- **GEN-07**: *Non-GET on Generation endpoints → **405 Method Not Allowed**.*  
- **GEN-08**: *Server error on Generation retrieval → **5xx**.*  
- **GEN-09**: *Cross-resource: items listed as introduced in a Generation reciprocate via their own `generation` field (where applicable); same for moves/types/abilities/species/version_groups; `main_region` reciprocates.*

---

## Versions

- **VER-01**: *Retrieve a Version by valid ID or name → **200 OK** with `names` and `version_group`.*  
- **VER-02**: *List Versions (no params) → default paginated list with `count`.*  
- **VER-03**: *Paginate Versions with `limit`/`offset` → correct page lengths and links.*  
- **VER-04**: *Version schema correctness: `id`, `name`, localized `names`, non-null `version_group` (named ref).*  
- **VER-05**: *Non-existent Version id/name → **404 Not Found**.*  
- **VER-06**: *Invalid pagination inputs on Version list → client error (prefer **400**) or consistent default.*  
- **VER-07**: *Non-GET on Version endpoints → **405 Method Not Allowed**.*  
- **VER-08**: *Server error on Version retrieval → **5xx**.*  
- **VER-09**: *Cross-resource: Version’s `version_group` reciprocates by listing this version; any external references to this version (e.g., in encounter/version details) resolve to a valid `/version/{name}`.*

---

### Global Non-Functional (Spec-Level) Checks

- **NFR-01**: *As an API consumer, I want typical read latencies to be reasonable for public use (if the docs mention any expectations), so that user experience is acceptable (observe & record; no strict SLOs stated in docs).*  
- **NFR-02**: *As an API consumer, I want reasonable resilience to transient network hiccups, so that brief timeouts or hiccups can be retried without data corruption (plan-level check; no tooling specifics).*  

---