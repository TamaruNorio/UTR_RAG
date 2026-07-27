---
title: "RF送信信号の制御"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.4"
command_group: "reader_control"
command_name: "RF送信信号の制御"
command_byte: "4Eh"
detail_command: "9Eh"
subcommand: null
operation_profile: "needs-metadata-confirmation"
operation_level: "reader-control"
rf_emission: true
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: true
requires_tag: false
requires_access_password: false
requires_parameters: true
verification_status: "REAL_DEVICE_VERIFIED_WITH_NOTES"
result_status: "REAL_DEVICE_PASS_WITH_NOTES"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-control"
  - "rf-emission"
  - "requires-parameters"
  - "pass-with-notes"
  - "rf-carrier-control"
---

# RF送信信号の制御

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **RF送信信号の制御** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.4`
- コマンド分類: リーダライタ制御
- 確認区分: `needs-metadata-confirmation`
- 操作レベル: リーダライタ制御
- コマンドバイト: `4Eh` / 詳細コマンド: `9Eh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、リーダライタが出力する **RF送信信号（キャリア）を OFF / ON / OFF→ON で制御すること** です。

`ON` または `OFF→ON` を指定するとRFキャリア出力に関係します。さらに、キャリアON維持状態ではRFタグのハンドル維持、4秒制限、キャリア休止時間、キャリア検知NACKなどが関係するため、単純なACKコマンドとして扱わず、状態遷移つきの高影響リーダライタ制御として実装してください。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | あり |
| 書き込み操作 | なし |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | なし |
| Accessパスワード確認 | なし |
| パラメータ確認 | あり |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 指定するRF送信信号制御値が `00h=OFF`、`01h=ON`、`02h=OFF→ON` のどれかを確認する。
4. `ON` / `OFF→ON` を実行する場合は、アンテナ接続、送信出力、周波数、キャリアセンス条件、周辺RF環境を確認する。
5. キャリアON維持状態でRFタグ通信を続ける場合は、対象タグが1枚に絞られるSelect条件・マスク条件を事前に確認する。
6. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件、復旧用の `OFF` 送信手順を決める。
7. NACK、timeout、フレーム不正、4秒経過、キャリア検知エラー時に、追加送信を続けない条件を決める。

## 6. PDF仕様フィールド定義

PDF原文の全文転記は `4e_9e_rf_carrier_control_raw.md` を参照してください。
このカードには、実装判断に必要な要点とAI向け構造化情報のみを残します。

## 7. コマンド形式・PDFフィールド定義の読み方

この節は、PDF 7.3.4 のコマンド表・ACK表・注意事項を、生成AIが実装に使える粒度へ分解したものです。完成HexはPDF掲載例として扱えますが、実機ログ由来のEPC/UII/TID/パスワードは公開しないでください。

### 7.1 送信コマンドフレーム

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス。共通通信フォーマットに従う |
| 2 | `CMD` | 1 | `4Eh` | リーダライタ制御コマンド |
| 3 | `LEN` | 1 | `02h` | DATA部は2byte |
| 4 | `DATA[0]` | 1 | `9Eh` | 詳細コマンド: RF送信信号の制御 |
| 5 | `DATA[1]` | 1 | `00h` / `01h` / `02h` | RF送信信号制御値 |
| 6 | `ETX` | 1 | `03h` | フレーム終端 |
| 7 | `SUM` | 1 | 可変 | `STX`から`ETX`までのSUM下位1byte |
| 8 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.2 RF送信信号制御値

| `DATA[1]` | 指定 | キャリア状態 | ハンドルへの影響 | 実装上の注意 |
|---|---|---|---|---|
| `00h` | `OFF` | キャリアOFF状態へ遷移 | 保持中のRFタグハンドルを破棄 | 復旧・終了時に使う。RF送信を止める意図で送る |
| `01h` | `ON` | キャリアON維持状態へ遷移 | 後続RFタグ通信で取得したハンドルを維持可能 | キャリア出力開始から最大4秒。すでにON維持状態で再度ONしても4秒制限は延長できない |
| `02h` | `OFF→ON` | 一度OFF後、キャリアON維持状態へ遷移 | OFF時に保持中ハンドルを破棄 | OFF時間は50msec以上。キャリアセンスを挟むため、ハンドル継続目的では使わない |

### 7.3 ACKレスポンス形式

PDF 7.3.4 のACKレスポンス表では、このコマンドの成功ACKは次の構造です。

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス |
| 2 | `CMD` | 1 | `30h` | ACK |
| 3 | `LEN` | 1 | `02h` | DATA部は2byte |
| 4 | `DATA[0]` | 1 | `9Eh` | 応答元の詳細コマンド |
| 5 | `DATA[1]` | 1 | 通常 `00h` | 将来拡張のための予約。独自解釈しない |
| 6 | `ETX` | 1 | `03h` | フレーム終端 |
| 7 | `SUM` | 1 | 可変 | `STX`から`ETX`までのSUM下位1byte |
| 8 | `CR` | 1 | `0Dh` | 改行終端 |

代表ACK Hex:

```text
02 00 30 02 9E 00 03 D5 0D
```

ACKを受けても、「現在キャリアが安全にONで維持され続ける」と固定判断しないでください。キャリアON維持は最大4秒であり、機種の間欠出力、キャリア休止時間、後続コマンドの処理時間、NACK条件に左右されます。

### 7.4 コマンド／レスポンス例

| 種別 | Hex | 説明 |
|---|---|---|
| 送信例 | `02 00 4E 02 9E 01 03 F4 0D` | `DATA[1]=01h` によりキャリアONを要求 |
| ACK例 | `02 00 30 02 9E 00 03 D5 0D` | `CMD=30h`、`DATA[0]=9Eh`、`DATA[1]=00h`予約 |

SUM確認:

| フレーム | SUM対象 | SUM下位1byte |
|---|---|---|
| 送信例 | `02+00+4E+02+9E+01+03` | `F4h` |
| ACK例 | `02+00+30+02+9E+00+03` | `D5h` |

### 7.5 キャリア状態とRFタグハンドル維持

| 状態 | キャリア出力 | ハンドル | 主な遷移 |
|---|---|---|---|
| キャリアOFF状態 | OFF | なし | `ON` または `OFF→ON` でON維持へ |
| キャリアON状態 | ON | コマンド単位 | RFタグ通信コマンド実行中の通常状態 |
| キャリアON維持状態 | ON | 後続RFタグ通信で維持可能 | 最大4秒、`OFF`・4秒経過・NACK等でOFF状態へ |

キャリアON維持状態で最初のRFタグ通信コマンドがRFタグのハンドルを取得すると、後続のRFタグ通信コマンドではInventory処理を省略して同じハンドルで通信できます。これにより処理時間を短縮できますが、対象タグが複数存在すると誤対象になる可能性があるため、Select条件などで1枚に絞ってください。

### 7.6 状態遷移・例外条件

| 条件 | 結果 | 実装アクション |
|---|---|---|
| キャリアOFF状態で `ON` | キャリアON維持状態へ | ACK後、最大4秒の制限をタイマ管理する |
| キャリアOFF状態で `OFF→ON` | OFF後にON維持状態へ | OFF時間50msec以上とキャリアセンス待ちを考慮する |
| キャリアON維持状態でRFタグ通信 | ON維持を継続し、ハンドルを維持 | 後続通信は同一タグ前提。対象タグをマスクで限定する |
| キャリアON維持状態で `ON` | 4秒制限は延長されない | 継続目的で使わない。PDFではNACK条件として扱う |
| キャリアON維持状態で `OFF→ON` | 一度OFFし、ハンドル破棄後にON | ハンドルを使い回す設計にしない |
| キャリアONから4秒経過 | コマンド実行中でもOFFへ | timeoutや途中終了と混同しない。ハンドルは破棄される |
| 一部機種の間欠出力中 | 前回ON時間と同じ時間だけ休止 | 休止中のコマンドは休止終了後に実行され、応答が遅れる可能性がある |

### 7.7 キャリアセンスとNACK条件

`ON` / `OFF→ON` ではキャリア出力前にキャリアセンスを行います。キャリアセンス待ち時間以内にキャリア出力を開始できない場合は、NACKレスポンスが返り、キャリアはOFFのままです。

| 条件 | NACK/状態 | 注意 |
|---|---|---|
| キャリア検知により出力不可 | NACK、エラーコード1 `60h` | `60h` はキャリア検知エラー。キャリア出力はOFFのまま |
| キャリアON維持状態で `ON` を再送 | NACK条件 | ON時間延長目的では使えない |
| キャリアON維持状態で出力レベル設定を変更 | 即時反映されない | 一度キャリアOFF状態に戻るまで変更は反映されない |
| RFタグ通信コマンドでNACK | ハンドル破棄 | 後続で同じタグに当たる保証がない。再Inventoryや条件再設定を検討する |

### 7.8 使用例の意味

PDF掲載の使用例では、事前にキャリアONにしてから `UHF_InventoryRead`、`UHF_SetSelectParam`、`UHF_BlockWrite`、`UHF_Read` を連続実行し、最後にキャリアOFFへ戻すことで、合計処理時間の短縮例を示しています。

| 方式 | PDF掲載の合計例 | 意味 |
|---|---:|---|
| RF送信信号の制御を使用 | 207msec | キャリアON維持とハンドル維持により、後続通信のInventory処理を省略できる場合がある |
| RF送信信号の制御を不使用 | 326msec | 各RFタグ通信コマンドで通常処理を行う |

この使用例は性能例であり、RFタグIC、タグ個体差、書き込み内部リトライ、周辺RF環境により変動します。運用前に実際のタグで確認してください。

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- フレーム不正
- キャリア検知エラー
- キャリア休止による応答遅延
- RFタグ通信中の後続レスポンス
- RFタグハンドル破棄後の再Inventory要否

NACKは共通NACK形式とPDF該当節を併せて確認してください。予約バイトは、PDFで意味が定義されていない限り、独自解釈しないでください。

ACK、後続レスポンス、可変長データの解釈は、コマンド番号だけで固定せず、`../../RESPONSE_AND_NACK_MASTER.md` の起動時スナップショットに基づいてください。ROM・機種、アンテナID出力、TID付加、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM/FLASH設定の状態により、ACKのタイミングや応答データ長が変わります。

### 8.1 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| フレーム長不一致、`STX/ETX/CR/SUM`不正 | `INVALID_FRAME` | 破棄し、必要なら再同期する |
| 受信期限内に1フレームも来ない | `TIMEOUT` | timeoutとして処理し、NACKとは分ける |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=30h` かつ `LEN=02h` かつ `DATA[0]=9Eh` | `ACK` | RF送信信号制御の成功ACK。`DATA[1]` は予約扱い |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中などの非同期タグ応答候補。通常ACKとは分離する |
| キャリア休止時間中に応答が遅れる | `DELAYED_RESPONSE_POSSIBLE` | timeout値設計時に機種仕様を考慮する |

対象識別子: コマンド `4Eh` / 詳細 `9Eh` / サブ `なし`。

### 8.2 ACK/レスポンス例

| 項目 | 内容 |
|---|---|
| 代表ACK Hex | `02 00 30 02 9E 00 03 D5 0D` |
| ACKデータ部 | `DATA[0]=9Eh`, `DATA[1]=00h` |
| `DATA[1]` | 将来拡張のための予約。通常 `00h`。成功状態やキャリア状態として独自解釈しない |
| タイミング注意 | 一部機種ではキャリア間欠出力により、キャリア休止時間後に実行・応答される場合がある |

### 8.3 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 9E 44 00 00 00 00 00 00 00 00 03 22 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコード |

### 8.4 このコマンドで特に見るNACK

| エラー | 意味 | 実装アクション |
|---|---|---|
| `error_code_1=60h` | キャリア検知エラー | キャリア出力はOFFのままと判断し、再送・チャンネル変更・環境確認は操作者判断にする |
| `FORMAT_ERROR` | 制御値、データ長、フレーム形式などの不正 | 送信フレーム生成を見直す。RF再送はしない |
| `SUM_ERROR` | SUM不一致 | フレーム生成を見直す。実機状態変更の有無をACKなしで断定しない |
| すでにON維持状態で `ON` | 4秒延長不可のNACK条件 | 継続目的なら設計を見直す。安易に連続送信しない |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、PDF定義の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.5 AI実装用レスポンス定義

#### 共通フレームoffset

| offset | フィールド | 実装上の意味 |
|---:|---|---|
| 0 | `STX` | 常に `02h`。異なる場合は `INVALID_FRAME` |
| 1 | `ADR` | 通常はリーダライタID。RFタグ応答でアンテナID出力ONの場合は読み取りANT番号 |
| 2 | `CMD` | `30h`=ACK、`31h`=NACK、`6Ch`=RFタグデータ、その他はPDF該当節で分類 |
| 3 | `LEN` | `DATA`部のbyte数。総フレーム長は `LEN + 7` |
| 4..`4+LEN-1` | `DATA` | ACK/NACK/タグ応答ごとの可変領域 |
| `4+LEN` | `ETX` | 常に `03h`。異なる場合は `INVALID_FRAME` |
| `5+LEN` | `SUM` | `STX`から`ETX`までのSUM下位1byte |
| `6+LEN` | `CR` | 常に `0Dh` |

#### ACK/データ部offset

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail_command` | `9Eh`。RF送信信号の制御に対するACK |
| 1 | `reserved` | 通常 `00h`。PDFで意味が定義されていないため独自解釈しない |

#### NACK分類

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象詳細コマンド `9Eh` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、キャリア検知エラーなどの主エラー |
| 2 | `error_code_2` | PDF定義がある場合のみ参照 |
| 3 | `error_code_3` | PDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
snapshot = read_startup_snapshot()
send_4e_9e(control_value)
frame = read_next_frame(timeout_with_carrier_rest_consideration)
if frame is None:
    return TIMEOUT
parsed = parse_common_frame(frame)
if parsed.invalid:
    return INVALID_FRAME
if parsed.cmd == 0x31:
    return parse_nack(parsed)
if parsed.cmd == 0x30 and parsed.len == 2 and parsed.data[0] == 0x9E:
    return ACK_RF_CARRIER_CONTROL(reserved=parsed.data[1])
return UNKNOWN_RESPONSE_REQUIRES_PDF_CHECK
```

#### 推奨パーサ出力

```json
{
  "frame_type": "ACK | NACK | RF_TAG_DATA | TIMEOUT | INVALID_FRAME | DELAYED_RESPONSE_POSSIBLE",
  "command": "RF送信信号の制御",
  "command_bytes": "4E 9E",
  "control_value": "00h | 01h | 02h",
  "carrier_state_assumption": "off | on_hold | unknown",
  "data_length": 2,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### 設定スナップショット必須項目

実行前に、ROM/機種、物理アンテナ容量、接続OKアンテナ、現在ANT、送信出力、使用周波数、キャリアセンス条件、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM/FLASH対象、現在推定キャリア状態を取得し、この結果をパーサへ渡してください。

## 9. 実機確認

実機確認区分: `needs-metadata-confirmation`

実機確認では、以下をログに残してください。

- 実行日時
- 操作者
- 対象機種
- ROMバージョン
- 接続方式
- 対象コマンド
- パラメータ
- 送信目的
- ACK/NACK/timeout
- エラーコード
- 復旧判断
- 結果状態

runtime logs、実CSVログ、顧客情報、実IPアドレス、raw EPC / UII / TID は GitHub にアップロードしないでください。必要な場合はマスク・要約して記録してください。

## 10. AIに実装・移植を依頼するときの注意

AIへ依頼するときは、次の前提を明示してください。

- 対象機種とROMバージョン
- 接続方式
- 実装言語
- このコマンドカード
- 関連ドキュメント
- 実機送信の有無
- 許可する操作範囲
- 禁止する操作範囲
- テスト方法
- 完了条件

実装言語は限定しません。Python、C#、C++、JavaScriptなど、対象環境に合わせて選択してください。

## 11. 参照ドキュメント

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。

