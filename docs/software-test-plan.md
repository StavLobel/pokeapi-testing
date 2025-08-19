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

| Resource Family | Operation | Params | Positive | Negative | Schema | Status | Pagination | Implementation Status |
|-----------------|-----------|--------|----------|----------|--------|--------|------------|----------------------|
| Pokémon         | GET /pokemon/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | 🎯 **COMPLETE** ✅ |
| Pokémon (list)  | GET /pokemon?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | 🎯 **COMPLETE** ✅ |
| Abilities       | GET /ability/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Abilities (list)| GET /ability?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Moves           | GET /move/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Moves (list)    | GET /move?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Types           | GET /type/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Types (list)    | GET /type?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Items           | GET /item/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Items (list)    | GET /item?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Berries         | GET /berry/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Berries (list)  | GET /berry?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Machines        | GET /machine/{id} | id | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Machines (list) | GET /machine?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Evolution       | GET /evolution-chain/{id} | id | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Evolution (list)| GET /evolution-chain?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Encounters      | GET /encounter/{id} | id | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Encounters (list)| GET /encounter?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Games           | GET /version/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Games (list)    | GET /version?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Locations       | GET /location/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Locations (list)| GET /location?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Regions         | GET /region/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Regions (list)  | GET /region?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Pokedexes       | GET /pokedex/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Pokedexes (list)| GET /pokedex?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Generations     | GET /generation/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Generations (list)| GET /generation?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |
| Versions        | GET /version/{id or name} | id, name | ✔ | ✔ | ✔ | 200,404 | N/A | ⏳ **PENDING** |
| Versions (list) | GET /version?limit&offset | limit, offset | ✔ | ✔ | ✔ | 200,400 | ✔ | ⏳ **PENDING** |

**Legend**: 
- 🎯 **COMPLETE** ✅ = All test cases implemented and passing
- ⏳ **PENDING** = Test cases defined but not yet implemented
- ✔ = Test type planned/required

---

## 6.1 Implementation Status

### 🎯 **COMPLETED RESOURCE FAMILIES**

#### **Pokémon Resource Family** ✅ **100% COMPLETE**
- **Status**: All 15 POK-XX test cases implemented and passing
- **Implementation**: `tests/api/test_pokemon.py`
- **Total Tests**: 56 test scenarios across 15 test methods
- **Coverage**: 4x parametrized coverage with different Pokémon (Bulbasaur, Pikachu, Mewtwo, Arceus)
- **Framework Enhancements**: 
  - Enhanced BaseAPIClient with HTTP methods (POST, PUT, DELETE, PATCH)
  - Enhanced PokemonAPIClient with comprehensive testing methods
  - Comprehensive test data for all scenarios
  - Robust validation helpers
- **Performance**: All tests pass in ~6.7 seconds
- **Test Cases**: POK-01 through POK-15 fully implemented

### ⏳ **PENDING RESOURCE FAMILIES**

#### **Abilities Resource Family** ⏳ **0% IMPLEMENTED**
- **Status**: Test cases defined but not yet implemented
- **Planned**: ABL-01 through ABL-10 test cases
- **Dependencies**: Framework ready (BaseAPIClient enhanced)

#### **Moves Resource Family** ⏳ **0% IMPLEMENTED**
- **Status**: Test cases defined but not yet implemented
- **Planned**: MOV-01 through MOV-10 test cases
- **Dependencies**: Framework ready (BaseAPIClient enhanced)

#### **Types Resource Family** ⏳ **0% IMPLEMENTED**
- **Status**: Test cases defined but not yet implemented
- **Planned**: TYP-01 through TYP-10 test cases
- **Dependencies**: Framework ready (BaseAPIClient enhanced)

#### **Other Resource Families** ⏳ **0% IMPLEMENTED**
- **Status**: Test cases defined but not yet implemented
- **Planned**: Items, Berries, Machines, Evolution, Encounters, Games, Locations, Regions, Pokedexes, Generations, Versions
- **Dependencies**: Framework ready (BaseAPIClient enhanced)

---

## 6.2 Framework Readiness

The testing framework is now **fully ready** for implementing other resource families:

✅ **BaseAPIClient**: Enhanced with all HTTP methods and headers support  
✅ **Test Infrastructure**: Robust pytest fixtures and configuration  
✅ **Validation Helpers**: Reusable test data and assertion methods  
✅ **CLI Override**: Dynamic base URL configuration for multi-environment testing  
✅ **Documentation**: Comprehensive test case definitions for all resource families  
✅ **Quality Standards**: All tests follow established patterns and best practices

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
