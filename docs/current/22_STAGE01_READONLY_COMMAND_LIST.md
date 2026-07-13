# Stage 0/1 Read-only Command List

Stage 0/1のread-only対象コマンドを以下に示す。Default executionはdry-runであり、実機通信には`--execute`と接続先指定が必要である。

| Stage | PDF section | Command name | Command byte | Detail command | Subcommand | Card path | Expected response | Device/ROM condition | Default execution | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Stage 0 | 7.3.1 | エラー情報の読み取り | 4Fh | 80h | - | docs/current/commands/cards/4f_80_read_error_info.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 低影響の状態確認 |
| Stage 0 | 7.3.8 | ROMバージョンの読み取り | 4Fh | 90h | - | docs/current/commands/cards/rom_version_read.md | ACK/NACK/timeout/no-response | 最初に実行し機種/シリーズ/ROMを判定 | dry-run | 標準フローの起点 |
| Stage 0 | 7.3.9 | チップバージョンの読み取り | 55h | 90h | - | docs/current/commands/cards/55_90_chip_version_read.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 機種/ROM条件を併記 |
| Stage 1 | 7.4.1 | リーダライタ動作モードの読み取り | 4Fh | 00h | - | docs/current/commands/cards/4f_00_read_reader_mode.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 設定変更は行わない |
| Stage 1 | 7.4.2 | UHF_GetSelectParam | 55h | 40h | - | docs/current/commands/cards/55_40_uhf_get_select_param.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | read-only parameter retrieval |
| Stage 1 | 7.4.3 | UHF_GetInventoryParam | 55h | 41h | - | docs/current/commands/cards/55_41_uhf_get_inventory_param.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | SetInventoryParamは対象外 |
| Stage 1 | 7.4.4 | UHF_GetExpandSelectParam | 55h | 42h | - | docs/current/commands/cards/55_42_uhf_get_expand_select_param.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | read-only parameter retrieval |
| Stage 1 | 7.4.5 | アンテナ切替設定の読み取り | 55h | 43h | 00h | docs/current/commands/cards/55_43_00_read_antenna_switching.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 読み取りのみ。切替設定変更は対象外 |
| Stage 1 | 7.4.6 | 出力設定の読み取り | 55h | 43h | 01h | docs/current/commands/cards/55_43_01_read_output_power.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 読み取りのみ。出力変更は対象外 |
| Stage 1 | 7.4.7 | 周波数設定の読み取り | 55h | 43h | 02h | docs/current/commands/cards/55_43_02_read_frequency.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 読み取りのみ。周波数変更は対象外 |
| Stage 1 | 7.4.8 | RFタグ通信関連パラメータの読み取り | 55h | 43h | 04h | docs/current/commands/cards/55_43_04_read_rf_tag_comm_params.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | read-only parameter retrieval |
| Stage 1 | 7.4.9 | EPC(UII)関連パラメータの読み取り | 55h | 43h | 05h | docs/current/commands/cards/55_43_05_read_epc_uii_params.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | read-only parameter retrieval |
| Stage 1 | 7.4.10 | 外部アンテナ自動切替設定の読み取り | 55h | 47h | - | docs/current/commands/cards/55_47_read_external_antenna_auto_switch.md | ACK/NACK/timeout/no-response | 8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET | dry-run | 読み取りのみ。自動切替設定変更は対象外 |
| Stage 1 | 7.4.11 | 汎用ポート値の読み取り | 4Fh | 9Fh | - | docs/current/commands/cards/4f_9f_read_general_port.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 外部I/O状態読み取り |
| Stage 1 | 7.4.12 | 拡張ポート値の読み取り | 4Fh | A0h | - | docs/current/commands/cards/4f_a0_read_extended_port.md | ACK/NACK/timeout/no-response | 8CH系のみ対象の可能性。対象機種非対応なら NOT_APPLICABLE_TO_TARGET | dry-run | 外部I/O状態読み取り |
| Stage 1 | 7.4.13 | FLASH設定値の読み取り(1バイトアクセス) | 4Fh | B4h | - | docs/current/commands/cards/4f_b4_read_flash_settings.md | ACK/NACK/timeout/no-response | ROM読み取りで機種判定後に実行 | dry-run | 読み取りのみ。FLASH書き込みは対象外 |
| Stage 1 | 7.4.14 | RSSIフィルタ設定の読み取り | 55h | 49h | - | docs/current/commands/cards/55_49_read_rssi_filter.md | ACK/NACK/timeout/no-response | ROM 2.100以降対象の可能性。非対応なら NOT_APPLICABLE_TO_TARGET | dry-run | read-only parameter retrieval |
| Stage 1 | 7.4.15 | アンテナ個別送信出力設定の読み取り | 55h | 4Ah | - | docs/current/commands/cards/55_4a_read_antenna_output_power.md | ACK/NACK/timeout/no-response | 8CH系またはROM条件依存の可能性。非対応なら NOT_APPLICABLE_TO_TARGET | dry-run | 読み取りのみ。出力変更は対象外 |
