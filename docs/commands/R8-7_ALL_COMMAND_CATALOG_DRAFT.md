# R8-7 All Command Catalog Draft

| No | コマンド分類 | コマンド名 | コマンド識別子 | RAG文書 | safety matrix | source traceability | PDF参照 | 安全分類 | 実機確認状態 | 網羅状態 | 備考 |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | reader_control | ROMバージョンの読み取り | 4F/90 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 実機では未送信 |
| 2 | uhf_basic_read | UHF_Inventory | 55/10 | あり | あり | あり | あり | INVENTORY_RF_EMISSION | HOLD | COVERED | Inventory系は未確認 |
| 3 | uhf_tag_memory_read | UHF_InventoryRead | 55/14 | あり | あり | あり | あり | INVENTORY_RF_EMISSION | HOLD | COVERED | 55h/14hの正対応 |
| 4 | uhf_parameter_read | UHF_GetInventoryParam | 55/41 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | ステータス取得系候補 |
| 5 | uhf_parameter_read | UHF_GetSelectParam | 55/40 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | ステータス取得系候補 |
| 6 | uhf_parameter_read | UHF_GetExpandSelectParam | 55/42 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | ステータス取得系候補 |
| 7 | uhf_parameter_write | UHF_SetInventoryParam | 55/31 | あり | あり | あり | あり | DEVICE_SETTING_RESTRICTED | PROHIBITED | COVERED | 自動送信禁止 |
| 8 | uhf_parameter_write | UHF_SetSelectParam | 55/30 | あり | あり | あり | あり | DEVICE_SETTING_RESTRICTED | PROHIBITED | COVERED | Select条件変更 |
| 9 | uhf_parameter_write | UHF_SetExpandSelectParam | 55/32 | あり | あり | あり | あり | DEVICE_SETTING_RESTRICTED | PROHIBITED | COVERED | Select条件変更 |
| 10 | antenna_inspection | UHF_CheckAntenna | 55/44 | あり | あり | なし | なし | NEEDS_SPEC_CONFIRMATION | NOT_TESTED | MISSING_TRACEABILITY | trace item不足 |
| 11 | antenna_setting_read | 使用アンテナ番号の読み取り | 55/48 | あり | あり | なし | なし | NEEDS_SPEC_CONFIRMATION | NOT_TESTED | MISSING_TRACEABILITY | trace item不足 |
| 12 | antenna_setting_write | 使用アンテナ番号の書き込み | 55/38 | あり | あり | なし | なし | DEVICE_SETTING_RESTRICTED | PROHIBITED | MISSING_TRACEABILITY | trace item不足 |
| 13 | reader_setting_read | 送信出力設定の読み取り | 55/43/01 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 出力変更ではない |
| 14 | reader_setting_read | アンテナ切替設定の読み取り | 55/43/00 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | アンテナ設定確認 |
| 15 | reader_setting_read | 外部アンテナ自動切替設定の読み取り | 55/47 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 8CH関連注意 |
| 16 | reader_setting_read | アンテナ個別送信出力設定の読み取り | 55/4A | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 出力値確認 |
| 17 | reader_setting_read | RSSIフィルタ設定の読み取り | 55/49 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 設定確認 |
| 18 | reader_setting_read | FLASH設定値の読み取り | 4F/B4 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 読み取りのみ |
| 19 | reader_setting_write | 送信出力設定の書き込み | 55/33/01 | あり | あり | あり | あり | RF_PARAM_CHANGE_RESTRICTED | PROHIBITED | COVERED | 送信出力変更禁止 |
| 20 | reader_setting_read | 周波数設定の読み取り | 55/43/02 | あり | あり | あり | あり | READ_ONLY | NOT_TESTED | COVERED | 設定確認 |
| 21 | reader_setting_write | 周波数設定の書き込み | 55/33/02 | あり | あり | あり | あり | RF_PARAM_CHANGE_RESTRICTED | PROHIBITED | COVERED | 周波数変更禁止 |
| 22 | reader_setting_write | アンテナ切替設定の書き込み | 55/33/00 | あり | あり | あり | あり | DEVICE_SETTING_RESTRICTED | PROHIBITED | COVERED | アンテナ設定変更禁止 |
| 23 | reader_setting_write | Accessパスワードの書き込み | 55/33/03 | あり | あり | あり | あり | TAG_MEMORY_WRITE_RESTRICTED | PROHIBITED | COVERED | 認証条件に影響 |
| 24 | reader_setting_write | 外部アンテナ自動切替設定の書き込み | 55/37 | あり | あり | あり | あり | DEVICE_SETTING_RESTRICTED | PROHIBITED | COVERED | 8CH自動切替禁止 |
| 25 | reader_setting_write | RSSIフィルタ設定の書き込み | 55/39 | あり | あり | あり | あり | DEVICE_SETTING_RESTRICTED | PROHIBITED | COVERED | 読取条件変更 |
| 26 | reader_setting_write | アンテナ個別送信出力設定の書き込み | 55/3A | あり | あり | あり | あり | RF_PARAM_CHANGE_RESTRICTED | PROHIBITED | COVERED | 送信出力変更禁止 |
| 27 | tag_memory_read | UHF_Read | 55/15 | あり | あり | あり | あり | READ_WITH_RF | HOLD | COVERED | 55h/15hの正対応 |
| 28 | tag_memory_write | UHF_Write | 55/16 | あり | あり | あり | あり | TAG_MEMORY_WRITE_RESTRICTED | PROHIBITED | COVERED | タグ書き込み |
| 29 | tag_memory_write | UHF_BlockWrite | 55/1A | あり | あり | あり | あり | TAG_MEMORY_WRITE_RESTRICTED | PROHIBITED | COVERED | タグ書き込み |
| 30 | tag_memory_write | UHF_BlockWrite2 | 55/1D | あり | あり | あり | あり | TAG_MEMORY_WRITE_RESTRICTED | PROHIBITED | COVERED | 大きい書き込み |
| 31 | tag_memory_destructive | UHF_BlockErase | 55/1B | あり | あり | あり | あり | PROHIBITED | PROHIBITED | COVERED | 破壊的操作 |
| 32 | tag_memory_destructive | UHF_Encode | 55/1E | あり | あり | あり | あり | PROHIBITED | PROHIBITED | COVERED | 破壊的操作 |
| 33 | tag_memory_destructive | UHF_Kill | 55/17 | あり | あり | あり | あり | PROHIBITED | PROHIBITED | COVERED | 破壊的操作 |
| 34 | tag_memory_destructive | UHF_Lock | 55/18 | あり | あり | あり | あり | PROHIBITED | PROHIBITED | COVERED | 破壊的操作 |
| 35 | arbitrary_or_passthrough_command | UHF_ThroughCmd | 55/FF | あり | あり | あり | あり | PROHIBITED | PROHIBITED | COVERED | 任意コマンド系 |
| 36 | persistent_reader_setting | FLASH書き込み | 4E/B4 | なし | あり | あり | あり | FLASH_WRITE_PROHIBITED | PROHIBITED | MISSING_RAG_DOC | canonical RAG path未登録 |
| 37 | persistent_reader_setting | FLASH初期化 | 4E/6F | なし | あり | なし | なし | FLASH_WRITE_PROHIBITED | PROHIBITED | HOLD | RAG pathとtrace item不足 |
| 38 | reader_control | リスタート | 4E/9D | あり | あり | なし | なし | DEVICE_SETTING_RESTRICTED | HOLD | MISSING_TRACEABILITY | trace item不足 |
