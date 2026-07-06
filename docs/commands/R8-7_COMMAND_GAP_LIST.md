# R8-7 Command Gap List

| No | 種別 | 対象コマンド | 問題内容 | 影響 | 推奨対応 | 優先度 | 次工程 | 備考 |
|---:|---|---|---|---|---|---|---|---|
| 1 | MISSING_TRACEABILITY | UHF_CheckAntenna | source_traceability_matrixにcommand trace itemが見当たらない | アンテナ確認系の根拠追跡が不十分 | PDF節・ページを確認しtrace itemを追加する | High | R8-8 | 実機送信対象にしない |
| 2 | MISSING_TRACEABILITY | 使用アンテナ番号の読み取り | source_traceability_matrixにcommand trace itemが見当たらない | アンテナ設定読取の根拠追跡が不十分 | PDF節・ページを確認しtrace itemを追加する | High | R8-8 | 機種依存注意 |
| 3 | MISSING_TRACEABILITY | 使用アンテナ番号の書き込み | source_traceability_matrixにcommand trace itemが見当たらない | 設定変更系の安全根拠追跡が不十分 | PDF節・ページを確認しtrace itemを追加する | High | R8-8 | PROHIBITED扱い |
| 4 | MISSING_TRACEABILITY | FLASH初期化 | source_traceability_matrixにcommand trace itemが見当たらない | 危険操作の根拠追跡が不十分 | PDF節・ページを確認しtrace itemを追加する | Critical | R8-8 | PROHIBITED扱い |
| 5 | MISSING_TRACEABILITY | リスタート | source_traceability_matrixにcommand trace itemが見当たらない | reader_control系の根拠追跡が不十分 | PDF節・ページを確認しtrace itemを追加する | Medium | R8-8 | 実機送信対象にしない |
| 6 | MISSING_RAG_DOC | FLASH書き込み | command_safety_matrixにcanonical RAG pathが未登録 | RAG文書への直接誘導が不足 | 既存章配下文書との対応を確認しcanonical pathを登録する | Critical | R8-8 | PROHIBITED扱い |
| 7 | MISSING_RAG_DOC | FLASH初期化 | command_safety_matrixにcanonical RAG pathが未登録 | RAG文書への直接誘導が不足 | 既存章配下文書との対応を確認しcanonical pathを登録する | Critical | R8-8 | PROHIBITED扱い |
| 8 | NEEDS_SPEC_CONFIRMATION | UHF_Read | 実機読取確認が未実施 | RC候補判断に進めない | タグ、アンテナ、既存設定、ログ方針を確定する | High | R8-8 | 55h/15h対応は確認済み |
| 9 | NEEDS_SPEC_CONFIRMATION | UHF_InventoryRead | 実機Inventory系確認が未実施 | RC候補判断に進めない | アンテナ構成、使用タグ、既存設定を確定する | High | R8-8 | 55h/14h対応は確認済み |
| 10 | PROHIBITED_CONFIRMATION | UHF_SetInventoryParam | 高リスク設定変更系として自動送信禁止 | 誤って実行候補にすると読取条件を変える可能性 | PROHIBITED/HOLD扱いを維持する | Critical | R8-8 | 実機送信対象にしない |
| 11 | PROHIBITED_CONFIRMATION | 周波数設定の書き込み | RF/地域設定に影響する可能性 | 法規・運用条件に影響 | PROHIBITED扱いを維持する | Critical | R8-8 | 実機送信対象にしない |
| 12 | PROHIBITED_CONFIRMATION | 送信出力設定の書き込み | RF出力に影響する可能性 | 法規・運用条件に影響 | PROHIBITED扱いを維持する | Critical | R8-8 | 実機送信対象にしない |
