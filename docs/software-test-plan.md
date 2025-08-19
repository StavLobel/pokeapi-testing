# Software Test Plan (STP) – PokéAPI v2

## 1. Overview and objectives

PokéAPI v2 is a publicly accessible, read-only REST service that exposes Pokémon-related data. The documentation states that the API is **consumption-only** and only the HTTP `GET` method is available [oai_citation:0‡pokeapi.co](https://pokeapi.co/docs/v2). There is no authentication, and rate limiting has been removed [oai_citation:1‡pokeapi.co](https://pokeapi.co/docs/v2).  

**Purpose of testing:**  
- Ensure endpoints behave exactly as documented.  
- Validate functional correctness, schema compliance, error handling, and pagination.  
- Mitigate risks of undocumented behavior, data drift, or broken cross-resource references.  

**Success criteria:**  
- All documented endpoints reliably return valid responses within expected schema and status codes.  
- Negative scenarios return safe and consistent error codes.  
- Cross-references between resources remain valid.  

---

## 2. Scope

**In scope (exactly as per docs):**
- Pokémon  
- Abilities  
- Moves  
- Types  
- Items  
- Berries  
- Machines  
- Evolution  
- Encounters  
- Games  
- Locations  
- Regions  
- Pokedexes  
- Generations  
- Versions  

**Out of scope:**  
- Any UI, private or undocumented endpoints, or authoring/updating resources (since API is read-only).  

---

## 3. References and Assumptions

**Documentation:**  
- [PokéAPI v2 Docs](https://pokeapi.co/docs/v2) (all resource sections)  

**Assumptions:**  
- **Authentication:** None (public, consumption-only).  
- **Rate limits:** Docs state no limits; assume safe but do not stress test.  
- **Caching:** Docs do not specify; caching semantics are unknown.  
- **Data volatility:** Some IDs/names may change if the dataset evolves; plan must tolerate shifts by using canonical examples from docs.  
- **Errors:** Error code semantics are not always documented; conservative assumption is 404 for invalid IDs/names, 405 for wrong HTTP methods.  

---

## 4. Test Approach

- Black-box, documentation-driven.  
- No reliance on implementation or backend data sources.  
- Only request/response pairs validated against published documentation.  

---

## 5. Test Types and Coverage

**Positive functional tests**  
- Retrieval by valid ID and valid name.  
- Listing with default, custom `limit` and `offset`.  
- Parameterized filters if explicitly documented.  

**Negative and boundary tests**  
- Invalid IDs (zero, negative, max+1, non-numeric, special chars).  
- Invalid names (typos, special chars).  
- Invalid query params (unknown keys, wrong types, out-of-range limits).  
- Unsupported HTTP methods (`POST`, `PUT`, `DELETE`).  
- Missing or invalid `Accept` headers.  

**Contract/schema tests**  
- Response body must match required fields, nesting, types, and constraints in docs.  
- Optional fields tested for presence/absence without breaking schema.  

**Status code tests**  
- 200 for successful retrieval.  
- 404 for non-existent IDs/names.  
- 405 for wrong method.  
- 415/422 for invalid media types or malformed requests (where applicable).  
- 5xx – treat as server errors; document occurrence but not reproducible expectation.  

**Pagination tests**  
- Validate `count`, `next`, `previous`, and `results`.  
- Boundary: `limit=0`, `limit=1`, `limit=max`, negative values, over-max.  
- Navigation through first, middle, and last page.  

**Data integrity / cross-resource tests**  
- Follow references (e.g., a Pokémon's ability → ability endpoint).  
- Ensure referenced resources exist and schemas match.  

**Non-functional checks**  
- Latency (if doc provided expectations – none documented).  
- Basic resilience against transient network errors.  

---

## 6. Endpoint Inventory and Coverage Matrix

| Resource Family | Operation | Params | Positive | Negative | Schema | Status | Pagination |
|-----------------|-----------|--------|----------|----------|--------|--------|------------|
| Pokémon         | GET /pokemon/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A |
| Pokémon (list)  | GET /pokemon?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ |
| Abilities       | GET /ability/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A |
| Abilities (list)| GET /ability?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ |
| …repeat for Moves, Types, Items, etc. | | | | | | | |

---

## 7. Test Data Strategy

- Use canonical examples from docs (e.g., `bulbasaur` for Pokémon, `stench` for ability).  
- Define lowest valid ID (1) and known upper bound per category (from docs where available).  
- Invalid data: -1, 0, large out-of-range (e.g., 99999), random strings.  
- Volatility: expect some IDs/names may be added in the future; maintain tests against doc examples.  

---

## 8. Entry and Exit Criteria

**Entry:**  
- Documentation available and stable.  
- Network connectivity to API.  
- Selected valid IDs/names confirmed.  

**Exit:**  
- 100% of endpoint families covered.  
- All happy-path tests pass.  
- All negative cases return documented error codes.  
- No open critical schema mismatches or consistency issues.  

---

## 9. Risk Analysis and Mitigations

| Risk | Mitigation |
|------|------------|
| API downtime | Schedule retries, mark test inconclusive not failed. |
| Data drift | Base deterministic tests on doc examples. |
| Rate limit changes | Monitor failures; adjust strategy. |
| Schema drift | Add schema validation at field level. |
| Pagination inconsistencies | Validate against count/next/previous contracts. |

---

## 10. Reporting and Triage

- Each defect logged with: endpoint, parameters, request, expected vs. actual, doc reference.  
- **Severity:**  
  - Critical: Endpoint unusable or schema broken.  
  - Major: Incorrect status code or missing required fields.  
  - Minor: Optional field discrepancy, doc mismatch.  
- **Priority:**  
  - P1: Blocks automation.  
  - P2: Major incorrectness.  
  - P3: Cosmetic/doc inconsistency.  

---

## 11. Traceability

| Objective | Endpoint Family | Test Types | Acceptance Criteria |
|-----------|----------------|------------|---------------------|
| Correct data retrieval | Pokémon, Abilities, etc. | Positive, Schema | Returns 200 with valid schema |
| Error handling | All | Negative, Status | Returns 404/405/400 appropriately |
| Pagination works | List endpoints | Positive, Negative | Correct `count`, `next`, `previous` |
| Data consistency | Cross-links | Integrity | References resolve to valid resources |

---

## 12. Acceptance Criteria

For **each endpoint family**:  
- **Positive:** Valid ID/name returns 200, schema matches docs.  
- **Negative:** Invalid ID/name returns 404; invalid param returns 400; wrong method returns 405.  
- **Schema:** All required fields present, correct types.  
- **Status codes:** Only documented codes allowed.  
- **Pagination:** `count` correct, navigation links valid, results length matches limit.  

If all families meet these criteria, the API passes this STP.

---
