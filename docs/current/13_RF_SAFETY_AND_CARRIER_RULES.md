# RF Safety And Carrier Rules

## 1. Japan domestic RF timing

The manual describes carrier output constraints for Japan domestic UHF operation:

- Stop emission within 4 seconds.
- Keep a transmit pause of at least 50 ms.
- Use at least 5 ms receive time for carrier sense before transmission.
- Carrier sense checks the target frequency channel before carrier output.

## 2. Carrier and LBT handling

When carrier sense cannot complete within the configured wait time, the reader/writer returns a NACK with CMD_LBT_ERROR. Log the command, target channel or scan mode, carrier sense wait, and received error code.

## 3. RF send signal and tag commands

RF送信信号の制御 can turn carrier state on or off according to command parameters. RF tag communication commands can start carrier output depending on current carrier state, command mode, automatic-reading mode, and antenna state.

## 4. Antenna diagnostics and switching

UHF_CheckAntenna and antenna-related settings are normal protocol functions. Confirm product class, ROM version, connected antenna count, target antenna number, internal/external antenna structure, and auto-switch range before use. Antenna disconnection can return CMD_ANT_ERROR.

## 5. 8CH and external antenna auto-switch

8CH antenna auto-switch and external antenna auto-switch are specification-defined features for applicable models. Treat them as parameterized functions. Confirm UTR-SUN02V-8CH versus UTR-SUN02-8CH behavior and external antenna numbering.

## 6. Multiple reader/writer operation

When multiple reader/writers use the same frequency, carrier output timing, carrier pause, carrier sense time, and scan mode must be coordinated to reduce collision and LBT errors.


## 7. Traceability use

- RF carrier, frequency, output power, antenna switching, LBT, and antenna error references should be traceable from relevant command cards.
- Antenna switching is a supported function, not a prohibited function.
- RF-impact commands should carry impact notes and response/error references.
