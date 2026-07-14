---
title: "Device ROM Identification And Support"
doc_type: "guide"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:[]
tags:
  - "utr-s201"
  - "guide"
---

# Device ROM Identification And Support

## 1. Standard identification flow

1. Connect to the reader/writer.
2. Execute ROM version read.
3. Parse the 4-byte ROM version number and the 5-byte series name.
4. Map the series name to the product type.
5. Consult the command support table for product and ROM version.
6. Confirm command parameters and field conditions.
7. Execute the target command.
8. Parse ACK, NACK, multiple responses, completion responses, or timeout.
9. Save the log.

## 2. Series mapping

| Series | Product |
| --- | --- |
| USM01 | UTR-S201 |
| USM02 | UTR-SUN02-4CH |
| USM05 | UTR-SHR201 |
| USM06 | UTR-SUN02V-8CH |
| USM08 | UTR-SUN02-8CH |

## 3. Ask the user only for field conditions

ROM can provide the series and ROM version when connected. Ask the user for conditions not available from ROM, such as connected antenna count, target antenna number, target tags, RAM-only or FLASH persistence intent, changed values, and site-acceptable operation.

## 4. ROM-dependent command groups

- UHF_GetHandle: ROM 2.050 or later.
- UHF_ThroughCmd: ROM 2.050 or later.
- RSSI filter read/write: ROM 2.100 or later.
- Antenna individual transmit output read/write: ROM 2.100 or later.
- External antenna auto-switch and extended ports: 8CH-class functions.
- Active antenna number read/write: 8CH-class functions.

## 5. 4CH and 8CH handling

UTR-SUN02-4CH and 8CH series differ in antenna and external-port handling. Do not infer 8CH support from a 4CH model. Do not treat antenna switching as unavailable in general; choose the command and parameter set that matches the product and ROM.


## 6. Traceability use

- ROM version read is the standard first traceability anchor for device identification.
- Series name to product mapping is used before applying device/ROM support.
- PDF 6.2 device support table should be referenced by command cards.
- 8CH-specific commands must identify USM06/USM08 handling where applicable.
