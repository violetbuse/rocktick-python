# Changelog

## 0.10.1 (2026-04-08)

Full Changelog: [v0.10.0...v0.10.1](https://github.com/violetbuse/rocktick-python/compare/v0.10.0...v0.10.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([add3377](https://github.com/violetbuse/rocktick-python/commit/add337704d13eee1481c1eeaf305b4d172251550))

## 0.10.0 (2026-03-27)

Full Changelog: [v0.9.3...v0.10.0](https://github.com/violetbuse/rocktick-python/compare/v0.9.3...v0.10.0)

### Features

* **internal:** implement indices array format for query and form serialization ([e2f1b61](https://github.com/violetbuse/rocktick-python/commit/e2f1b61fe0e45af5cb9f8f05e7165ae6408190a1))


### Chores

* **ci:** skip lint on metadata-only changes ([69b4454](https://github.com/violetbuse/rocktick-python/commit/69b4454f924b57eaeef578225ebe67b2b68f231f))
* **internal:** update gitignore ([4ed79fa](https://github.com/violetbuse/rocktick-python/commit/4ed79fad681dbf165bc844d553ed11821878c7a7))

## 0.9.3 (2026-03-20)

Full Changelog: [v0.9.2...v0.9.3](https://github.com/violetbuse/rocktick-python/compare/v0.9.2...v0.9.3)

### Bug Fixes

* sanitize endpoint path params ([e9650c3](https://github.com/violetbuse/rocktick-python/commit/e9650c327e305cd02be52b5636bf792b449ec13f))


### Chores

* **internal:** tweak CI branches ([c672607](https://github.com/violetbuse/rocktick-python/commit/c6726077865957b1ab38e17f1f059803fabcc10a))

## 0.9.2 (2026-03-17)

Full Changelog: [v0.9.1...v0.9.2](https://github.com/violetbuse/rocktick-python/compare/v0.9.1...v0.9.2)

### Bug Fixes

* **deps:** bump minimum typing-extensions version ([2c1bf5b](https://github.com/violetbuse/rocktick-python/commit/2c1bf5b0253919984abe475299719390aa2b54b6))

## 0.9.1 (2026-03-17)

Full Changelog: [v0.9.0...v0.9.1](https://github.com/violetbuse/rocktick-python/compare/v0.9.0...v0.9.1)

### Bug Fixes

* **pydantic:** do not pass `by_alias` unless set ([374658b](https://github.com/violetbuse/rocktick-python/commit/374658bb78baf34590bd5a797738a389bf8ff90a))


### Chores

* **ci:** bump uv version ([e6bd1af](https://github.com/violetbuse/rocktick-python/commit/e6bd1afcc31ec8b4eee05183e26f83f392205238))
* **ci:** skip uploading artifacts on stainless-internal branches ([eb8b5f9](https://github.com/violetbuse/rocktick-python/commit/eb8b5f9b8a137cea1d4641052f9639bdaf50b77c))
* format all `api.md` files ([1a024e5](https://github.com/violetbuse/rocktick-python/commit/1a024e53c6719ca8223494a3516f31a2f9f796a3))
* **internal:** add request options to SSE classes ([62779c7](https://github.com/violetbuse/rocktick-python/commit/62779c7ab3d3fc50ef13426b64a80fc90c77669c))
* **internal:** bump dependencies ([d4f5cfb](https://github.com/violetbuse/rocktick-python/commit/d4f5cfb6d308400f76a694a0ef2609ec97363f60))
* **internal:** fix lint error on Python 3.14 ([7520614](https://github.com/violetbuse/rocktick-python/commit/7520614632b527f45e04d960e9c1bf138a859ce1))
* **internal:** make `test_proxy_environment_variables` more resilient ([47d36b9](https://github.com/violetbuse/rocktick-python/commit/47d36b9edb9916aa205a4281bb20b3af111e4c96))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([57a7b7b](https://github.com/violetbuse/rocktick-python/commit/57a7b7b9621b4f4921d281194191e8c00dad8fc2))
* **internal:** remove mock server code ([ad94b3d](https://github.com/violetbuse/rocktick-python/commit/ad94b3dcb480420c5fb8d1fd988d6d3ab1840f81))
* update mock server docs ([0c642ee](https://github.com/violetbuse/rocktick-python/commit/0c642ee29d48ad8c0f023d77e630bb55038571b3))

## 0.9.0 (2026-01-30)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/violetbuse/rocktick-python/compare/v0.8.0...v0.9.0)

### Features

* **client:** add custom JSON encoder for extended type support ([8d66182](https://github.com/violetbuse/rocktick-python/commit/8d661822ece182a5fa0b4c7e383405b7b96fd992))


### Chores

* **ci:** upgrade `actions/github-script` ([251e639](https://github.com/violetbuse/rocktick-python/commit/251e639486fe301a2675b4749ef32e938cf7ab03))
* **internal:** update `actions/checkout` version ([763a093](https://github.com/violetbuse/rocktick-python/commit/763a093fb351848416f01fb0b9e300a40ea73692))

## 0.8.0 (2026-01-14)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/violetbuse/rocktick-python/compare/v0.7.0...v0.8.0)

### Features

* **client:** add support for binary request streaming ([abe56bb](https://github.com/violetbuse/rocktick-python/commit/abe56bbd152c227dcb315c0c4763e58124002c18))


### Chores

* **internal:** codegen related update ([90dc336](https://github.com/violetbuse/rocktick-python/commit/90dc33628b0d6a025e8feeafc089db22399923a7))

## 0.7.0 (2025-12-19)

Full Changelog: [v0.6.2...v0.7.0](https://github.com/violetbuse/rocktick-python/compare/v0.6.2...v0.7.0)

### Features

* **api:** changed production from rocktick.com to cloud.rocktick.com ([0cf7b52](https://github.com/violetbuse/rocktick-python/commit/0cf7b52c43101e1bc152d93a356b2babf28ca7f5))

## 0.6.2 (2025-12-19)

Full Changelog: [v0.6.1...v0.6.2](https://github.com/violetbuse/rocktick-python/compare/v0.6.1...v0.6.2)

### Chores

* **internal:** add `--fix` argument to lint script ([c80825f](https://github.com/violetbuse/rocktick-python/commit/c80825f199e8fa9210b54ed2c0881a4396db1620))

## 0.6.1 (2025-12-18)

Full Changelog: [v0.6.0...v0.6.1](https://github.com/violetbuse/rocktick-python/compare/v0.6.0...v0.6.1)

### Bug Fixes

* use async_to_httpx_files in patch method ([2ea8b77](https://github.com/violetbuse/rocktick-python/commit/2ea8b77688fa9c92403a4190f338f34de81759d2))

## 0.6.0 (2025-12-17)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/violetbuse/rocktick-python/compare/v0.5.0...v0.6.0)

### Features

* **api:** added tenant id to client settings ([fa64303](https://github.com/violetbuse/rocktick-python/commit/fa643031303e769f122bfeeb82c145f2bdec720c))


### Chores

* **internal:** add missing files argument to base client ([1dcd778](https://github.com/violetbuse/rocktick-python/commit/1dcd778d7d9c168ae6794bf596ed339691633e9c))
* speedup initial import ([fa0591d](https://github.com/violetbuse/rocktick-python/commit/fa0591da49172b00e4141cd5e852fc7f27faa1cc))


### Refactors

* **internal:** switch from rye to uv ([c418694](https://github.com/violetbuse/rocktick-python/commit/c418694f535c76300a4cb4a6a75d9f0c9ca70dfa))

## 0.5.0 (2025-12-15)

Full Changelog: [v0.1.20...v0.5.0](https://github.com/violetbuse/rocktick-python/compare/v0.1.20...v0.5.0)

### Features

* **api:** api update ([3d65476](https://github.com/violetbuse/rocktick-python/commit/3d65476589efb45ddb0c7f2f16b46556e16bf225))
* **api:** changed models request and response to HttpRequest and HttpResponse ([3e324fc](https://github.com/violetbuse/rocktick-python/commit/3e324fc29ddf07766f1f6c4401f08eca2c721e67))


### Bug Fixes

* **api:** changed names also to http_request and http_response ([4d59cf9](https://github.com/violetbuse/rocktick-python/commit/4d59cf92fe5890f9a171c9b1a5706d5873d5d48f))

## 0.1.20 (2025-12-14)

Full Changelog: [v0.0.1...v0.1.20](https://github.com/violetbuse/rocktick-python/compare/v0.0.1...v0.1.20)

### Features

* **api:** changed local dev url port ([ff84fad](https://github.com/violetbuse/rocktick-python/commit/ff84fade77015ef110e3edea573742fb6e0b205d))


### Chores

* configure new SDK language ([1af9dad](https://github.com/violetbuse/rocktick-python/commit/1af9dad5ccc10bbeeaf5795e48715ff0850afca6))
* update SDK settings ([55f2206](https://github.com/violetbuse/rocktick-python/commit/55f22063d854b20930b7495284436a69209eed94))
* update SDK settings ([6832898](https://github.com/violetbuse/rocktick-python/commit/68328987164caf77785dd4fc76e75adcf8cb177e))
