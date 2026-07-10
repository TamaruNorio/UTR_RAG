# Parameter Confirmation Guide

## 1. Automatically obtainable by ROM read

- Product series
- Product type
- ROM version

## 2. Ask the user

- Connected antenna count
- Antenna number to use
- Auto-switch target antenna range
- Target RF tags
- Memory bank
- Word address
- Word count
- Write data
- RAM change or FLASH persistence
- Frequency or scan mode
- Transmit output level
- Reader/writer operation mode
- External I/O purpose
- Recovery method requirements

## 3. Question template

- Target product and ROM were identified as `<series>/<ROM>`. Which antenna ports are physically connected?
- Which operation do you want: read-only, setting change, RF tag read, RF tag write, Lock/Kill, or external I/O?
- For tag memory operations, which target tag, memory bank, word address, word count, and password condition should be used?
- For settings, should the change be RAM-only or persisted to FLASH?
- What recovery value or rollback procedure should be logged?

## 4. Missing parameter response

If a required parameter is missing, return a parameter checklist instead of producing a completed frame or device-sendable code.
