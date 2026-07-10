# Response And NACK Master

Target specification: UTR-S201シリーズ 通信プロトコル説明書 Ver.1.17.

## 1. Communication format

Chapter 5 defines the common frame. AI assistance must keep frame structure, response type, timeout policy, and SUM calculation concept separate. This package does not include completed Hex or SUM-calculated commands.

## 2. Response principles

- Command mode responses must be classified as ACK, NACK, multiple response, completion response, timeout, or command-specific no-response behavior.
- Automatic-reading mode responses are asynchronous and must be handled with a receive loop.
- RF tag commands can produce multiple tag responses before an end or timeout condition.
- Completion responses must be parsed when the command section defines one.
- Timeout is not the same as NACK; log it separately.

## 3. Common NACK response

Section 7.6 defines common NACK response. The response contains the detail command associated with the error and error code 1 through error code 4. Reserved bytes can contain non-zero values but should be ignored unless the specification assigns meaning.

## 4. Error code 1

| Code | Symbol | Meaning |
| --- | --- | --- |
| 01h | CMD_CRC_ERROR | RF tag receive CRC mismatch |
| 02h | CMD_TIME_OVER | RF tag receive data interrupted |
| 03h | CMD_RX_ERROR | Anti-collision processing error |
| 04h | CMD_RXBUSY_ERROR | No RF tag response |
| 07h | CMD_ERROR | Internal reader/writer command error |
| 0Ah | CMD_UHF_IC_ERROR | Built-in UHF IC returned RF tag access error |
| 60h | CMD_LBT_ERROR | Carrier sense timeout; carrier could not start |
| 64h | HARDWARE_ERROR | Hardware internal error |
| 68h | CMD_ANT_ERROR | Antenna disconnection related error |
| 42h | SUM_ERROR | SUM value invalid |
| 44h | FORMAT_ERROR | Command format or parameter invalid |

## 5. Error code 2 and 4

Error code 2 is mainly used when error code 1 is CMD_UHF_IC_ERROR. Error code 4 is mainly used for UHF_BlockWrite2 when error code 3 indicates UHF IC error. Important values include unsupported, insufficient privileges, memory overrun, memory lock, cryptographic error, response buffer overflow, insufficient power, write failure, kill failure, lock failure, not detected, handle acquisition failure, Access password error, and CRC error.

## 6. Error code 3

For UHF_Encode, error code 3 identifies the failed internal operation, including Reserved-area write, EPC(UII)-area write, User-area write, and Lock command issuance. For UHF_BlockWrite2, error code 3 participates in partial-failure diagnostics.

## 7. Command-specific notes

- UHF_Encode can update multiple memory banks and Lock state; partial completion must be considered.
- UHF_BlockWrite2 can fail partway through multi-word or multi-area operations.
- Lock and Kill can have irreversible effects on the tag.
- UHF_ThroughCmd requires ROM support and command-specific receive handling.
- RF carrier and antenna errors must be logged separately from tag memory errors.
