# AI Implementation Guardrails

## 1. Core behavior

- AI does not arbitrarily mark protocol-defined commands as unavailable.
- Commands listed in the protocol manual are organized as usable when target device, ROM, parameters, impact, response handling, and recovery conditions are understood.
- When connected, the first standard step is ROM version read to identify product series and ROM version.
- Ask the user for field conditions and missing parameters that ROM cannot provide.

## 2. Output constraints

- Do not output completed Hex frames.
- Do not output SUM-calculated commands.
- Do not immediately generate device-sendable code.
- Separate desk review from real-device confirmation.

## 3. Before implementation

Before assisting implementation, organize purpose, target device/ROM, parameters, RAM/FLASH impact, RF impact, tag-memory impact, ACK response, NACK response, timeout behavior, and recovery method.

## 4. Receive handling

Implementation guidance must distinguish ACK, NACK, multiple responses, completion responses, asynchronous responses, no-response cases, and timeout. NACK error codes 1 through 4 should be parsed according to section 7.6.

## 5. Positioning

This package is an AI-ready no-PDF RAG package for Ver.1.17 desk use. It is not a replacement for the official PDF and is not a formal external release or production guarantee.


## 6. Traceability use

- AI must not treat missing traceability as permission to guess.
- AI should cite command-card traceability fields before implementation guidance.
- When traceability is NEEDS_*_TRACE, implementation guidance should state the missing trace explicitly.
- AI should not generate executable code directly from incomplete traceability.
