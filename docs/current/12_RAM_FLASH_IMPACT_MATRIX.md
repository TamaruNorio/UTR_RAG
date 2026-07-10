# RAM FLASH Impact Matrix

## 1. Classification

| Area | Typical commands | Impact | Recovery / confirmation |
| --- | --- | --- | --- |
| Command-mode parameters | Reader/writer mode, RF tag communication parameters, EPC(UII) parameters | RAM or configured target area changes | Read current value first and log intended target |
| Automatic-reading parameters | Select, Inventory, ExpandSelect, mode parameters | Affects asynchronous reading behavior | Confirm mode, session, Q value, select mask, and timeout |
| FLASH data | FLASH setting read/write, FLASH initialize, selected persistent settings | Persistent across restart when written to FLASH | Read before change, record old/new values, define restore path |
| RAM-only changes | Temporary operating parameters | Lost on restart if not persisted | Log expected lifetime |
| RAM/FLASH interaction | Settings with RAM and FLASH reflection rules | Can differ by parameter and ROM version | Confirm source, target, and reflection behavior |
| Access password | Access password write and tag operations | Affects protected tag access | Confirm password handling and masking |
| RSSI filter | RSSI filter read/write | Affects tag response filtering | Confirm ROM 2.100 or later and threshold intent |
| Inventory timeout | Inventory-related parameters | Affects receive loop and completion timing | Confirm ROM behavior and timeout policy |
| Command timeout | Reader/writer command timeout | Affects NACK/timeout timing | Avoid unnecessarily large values and log timeout policy |

## 2. Impact handling

Protocol-defined commands are organized by impact and recovery requirements. Setting changes, FLASH persistence, RF output, antenna switching, tag memory writes, Lock, Kill, and external I/O changes should include before/after confirmation and a recovery note where applicable.


## 3. Traceability use

- Each command card should link to the RAM/FLASH impact category.
- If impact is not explicit, use NEEDS_RAM_FLASH_TRACE.
- Setting write commands should distinguish RAM-only effect and FLASH/persistent effect where possible.
- FLASH initialization and FLASH one-byte write require recovery notes.
