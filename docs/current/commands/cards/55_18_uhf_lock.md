---
title: "UHF_Lock"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.6"
command_group: "rf_tag_communication"
command_name: "UHF_Lock"
command_byte: "55h"
detail_command: "18h"
subcommand: null
operation_profile: "tag-memory-or-high-impact"
operation_level: "write/configuration"
rf_emission: true
write_operation: true
flash_operation: false
tag_memory_operation: true
requires_rom_check: true
requires_antenna: true
requires_tag: true
requires_access_password: true
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
  - "rf-tag-communication"
  - "rf-emission"
  - "write-operation"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "access-password"
  - "pass-with-notes"
  - "uhf-lock"
---

# UHF_Lock（タグメモリロック）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_Lock** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.6`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `18h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_Lock** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | あり |
| 書き込み操作 | あり |
| FLASH操作 | なし |
| タグメモリ操作 | あり |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | あり |
| Accessパスワード確認 | あり |
| パラメータ確認 | あり |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 読み取り専用か、設定変更か、タグメモリ操作かを分類する。
4. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。
5. 周波数、送信出力、アンテナ設定、FLASH、タグメモリに影響する場合は、事前承認を取る。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.5.6` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.6   UHF_Lock
  RFタグへの読み書きができないようにロックを[設定]／[解除]するコマンドです。

  本コマンドを実行すると、ISO18000-63 規格で規定された、[Select], [Query], [Access], [Lock]など
  のコマンドを、リーダライタが自動的に順次実行します。
    ※リーダライタと RF タグ間で実行されるコマンドの詳細は、
                                 「3.10 RF タグ通信コマンド実行時の
     リーダライタの内部処理」をご参照ください。
    ※読み書き対象の RF タグが 1 枚となるように、あらかじめ[Select]コマンドのマスク条件や
     [Query]コマンドのパラメータを設定した状態で本コマンドを実行してください。
     複数の RF タグが応答を返す状態でコマンドを実行すると、意図しない RF タグに対して
     コマンドが実行されたり、コマンドの実行に失敗したりする可能性があります。
    ※本コマンドは、リーダライタの Access パスワードにあらかじめ[0000 0000]以外が設定された
     状態で実行する必要があります。

  RFタグのロックを[設定]／[解除]するためには、RFタグのAccess Password領域(Reserved領域の
  Wordアドレス[02]hから2[Word])に、[0000 0000]h以外のAccess Passwordを書き込んだ状態で
  [UHF_Lock]コマンドを実行し、リーダライタに設定されたAccessパスワードと、RFタグに書き込
  まれたAccess Passwordが一致する必要があります。
    ※1：リーダライタに設定するパスワードは、[Accessパスワードの書き込み]コマンドを
       使用しておこないます。
    ※2：RFタグへ設定するパスワードは、[UHF_Write]コマンドまたは[UHF_BlockWrite]コマンド
       を使用して事前に書き込みます。


［コマンド］
ラベル名 バイト数                                    内容
 STX   1         02h
アドレス   1         00h（ 「5.2 通信フォーマットの詳細」参照）
コマンド   1         55h
データ長   1         04h
       1         18h（詳細コマンド）
                 パラメータ 1
                  ビット             処理対象              処理種別             フラグ
                 bit0     TID 領域               PermaLock            Mask
                 bit1     TID 領域               PasswordWrite        Mask
                 bit2     EPC 領域               PermaLock            Mask
            1
                 bit3     EPC 領域               PasswordWrite        Mask
                 bit4     Access Password 領域   PermaLock            Mask
                 bit5     Access Password 領域   PasswordRead/Write   Mask
                 bit6     Kill Password 領域     PermaLock            Mask
                 bit7     Kill Password 領域     PasswordRead/Write   Mask
                 パラメータ 2
                  ビット             処理対象              処理種別             フラグ
                 bit0     EPC 領域               PermaLock            Action
                 bit1     EPC 領域               PasswordWrite        Action
データ部             bit2     Access Password 領域   PermaLock            Action
            1
                 bit3     Access Password 領域   PasswordRead/Write   Action
                 bit4     Kill Password 領域     PermaLock            Action
                 bit5     Kill Password 領域     PasswordRead/Write   Action
                 bit6     User 領域              PermaLock            Mask
                 bit7     User 領域              PasswordWrite        Mask
                 パラメータ 3
                  ビット             処理対象              処理種別             フラグ
                 bit0     0 固定
                 bit1     0 固定
                 bit2     0 固定
            1
                 bit3     0 固定
                 bit4     User 領域              PermaLock            Action
                 bit5     User 領域              PasswordWrite        Action
                 bit6     TID 領域               PermaLock            Action
                 bit7     TID 領域               PasswordWrite        Action
 ETX        1    03h
 SUM        1    SUM 値（  「5.3 SUM の計算方法」参照）
  CR        1    0Dh


＜コマンドパラメータ＞
  各 bit にアサインされている「処理対象」「処理種別」「フラグ」について説明します。

  ● 処理対象と処理種別
     [Lock]コマンドの処理対象となる領域が以下の 5 種準備されており、            それぞれの領域に対して、
     「PasswordWrite」または「PasswordRead/Write」、
                                           「PermaLock」を実行することができま
     す。
            処理種別                              具体的な処理内容
                            ・Access パスワード認証無しの場合
                              Read は可能だが Write は不可
      PasswordWrite         ・Access パスワード認証有りの場合
                              Read も Write も可能
                            ・Lock 状態は[設定]または[解除]に変更が可能。
                            ・Access パスワード認証無しの場合
                              Read も Write も不可
      PasswordRead/Write    ・Access パスワード認証有りの場合
                              Read も Write も可能
                            ・Lock 状態は[設定]または[解除]に変更が可能。
                            設定した Lock 状態（解除／設定）を変更不可とする。
                            Lock 状態は恒久的に保持され、変更はできません。
                            ・Lock 状態が[解除]された状態で PermaLock すると、
      PermaLock
                              Lock 状態を[設定]に変更できなくなる。
                            ・Lock 状態が[設定]された状態で PermaLock すると、
                              Lock 状態を[解除]に変更できなくなる。

              処理対象                    設定可能な処理種別
                               Password Write
       EPC 領域
                               PermaLock
                               Password Write
       TID 領域
                               PermaLock
                               Password Write
       User 領域
                               PermaLock
                               Password Read/Write
       Access Password 領域
                               PermaLock
                               Password Read/Write
       Kill Password 領域
                               PermaLock
  ※：Write Lock とは、Read はできるが Write はできない状態です。
    ・Access パスワードの認証無しの場合、Read はできますが、Write はできません。
    ・Access パスワードの認証有りの場合、Read も Write も可能となります。
  ※：Read/Write Lock とは、Read も Write もできない状態です。
    ・Access パスワードの認証無しの場合、Read も Write もできません。
    ・Access パスワードの認証有りの場合、Read も Write も可能となります。
  ※：PermaLock を実行しなければ、Write Lock 状態または Read/Write Lock 状態を何度でも[設
    定]／[解除]することが可能です。  （事前の Access パスワード認証が必要）
  ※：PermaLock 実行後は、Lock 状態（[設定]／[解除]）を変更することができなくなります。
       ・Write Lock を[設定]した状態で PermaLock を実行すると、その領域に対する
        Write ができなくなり、Write Lock の[解除]ができない状態となります。
       ・Write Lock を[解除]した状態で PermaLock を実行すると、その領域に対する
        Write できますが、Write Lock が[設定]できない状態となります。


  ● フラグ
     上記「処理対象+処理種別」ごとに、2 つのフラグが準備されています。
     各フラグを「0」または「1」にセットすることで、処理内容が変わります。

       フラグ       セットする値                   処理内容
                           指定した「処理対象+処理種別」に対し、
                     0
                           Action の値を書き込まない
        Mask
                           指定した「処理対象+処理種別」に対し、
                     1
                           Action の値を書き込む
                     0     Lock の[解除]を実行
       Action
                     1     Lock の[設定]を実行
     [Mask]フラグが 1 にセットされた「処理対象+処理種別」のみ、同じ「処理対象+処理種別」
     の[Action]の値が RF タグに書き込まれます。

     ※Lock 状態を[設定]も[解除]もしない領域に対しては、[Mask=0]のフラグとしてコマンドを
      実行します。[Action]は 0 でも 1 でも結果は変わりません。
                    「処理対象+処理種別」のフラグを、[Mask=1], [Action=1]に
     ※Lock を[設定]する場合、
      セットして実行します。
                    「処理対象+処理種別」のフラグを、[Mask=1], [Action=0]に
     ※Lock を[解除]する場合、
      セットして実行します。
     ※処理種別が PermaLock の場合、一度 Lock 状態を[設定]すると、その後[Mask=1],
     [Action=0]として再度実行しても、PermaLock を[解除]することはできません。


＜注意事項＞
 [UHF_Lock]コマンドを実行した直後は、リーダライタおよび RF タグに同じ Access パスワードが
 書き込まれた状態となっているため、[UHF_Lock]コマンドで Write Lock を設定しても、直後に
 [UHF_Write]コマンドや[UHF_BlockWrite]コマンドを実行した場合に書き込める場合があります。

  [UHF_Lock]コマンドを使わない時は、[Access パスワードの書き込み]コマンドを使用して、リー
  ダライタ側の Access パスワードを[0000 0000]h に戻してください。

    ※リーダライタ側の Access パスワードを設定したままにすると、異なる Access パスワードを持
     つ RF タグや、Access パスワードが設定されていない RF タグに対して、読み書きができなく
     なります。
    ※リーダライタの電源を切ったり、[リスタート]コマンドを実行したりした場合にも、Access パ
     スワードは[0000 0000]h に戻ります。


［ACK レスポンス］
ラベル名 バイト数                                       内容
 STX         1      02h
アドレス         1      00h（「5.2 通信フォーマットの詳細」参照）
 ACK         1      30h
データ長         1      01h
データ部         1      18h（詳細コマンド）
 ETX         1      03h
 SUM         1      SUM 値（「5.3 SUM の計算方法」参照）
  CR         1      0Dh


［NACK レスポンス］
 「7.6 NACK レスポンスとエラーコード」参照。


［コマンド／レスポンス例］
    (例 1) User 領域の Password Write Lock を[設定]する場合
         データ種類            処理対象              処理種別          フラグ       コマンド列
        パラメータ 1               ―               ―             ―         00
        パラメータ 2        bit7: User 領域     PasswordWrite   Mask=1       80
        パラメータ 3        bit5: User 領域     PasswordWrite   Action=1     20

    Mask=1 が設 定されている領域の み Action が実行されま す。上記の場合、 User 領域の
    PasswordWrite の Action が実行されます。その他の領域の Lock 状態は変更されません。
    User 領域の PasswordWrite の Action=1 のため、User 領域の PasswordWrite が[設定]されます
    （Lock された状態となります）        。
    • コマンド
       02 00 55 04 18 00 80 20 03 16 0D
    • レスポンス
       02 00 30 01 18 03 4E 0D


    (例 2) User 領域の Password Write Lock を[解除]する場合
         データ種類            処理対象              処理種別          フラグ       コマンド列
        パラメータ 1               ―               ―             ―         00
        パラメータ 2        bit7: User 領域     PasswordWrite   Mask=1       80
        パラメータ 3        bit5: User 領域     PasswordWrite   Action=0     00

    Mask=1 が設 定されている領域の み Action が実行されま す。上記の場合、 User 領域の
    PasswordWrite の Action が実行されます。その他の領域の Lock 状態は変更されません。
    User 領域の PasswordWrite の Action=0 のため、User 領域の PasswordWrite が無効となりま
    す（Lock が解除された状態となります）           。
    • コマンド
       02 00 55 04 18 00 80 00 03 F6 0D
    • レスポンス
       02 00 30 01 18 03 4E 0D
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

このカードでは、以下を意図的に記載しません。

- 実機へそのまま送信できる完成Hex
- SUM計算済みの送信用コマンド例
- 安全ガードを省略した実装コード

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- ACK
- NACK
- timeout
- 無応答
- 複数レスポンス
- 完了レスポンス
- LBTエラー
- アンテナ関連エラー
- UHF ICエラー

NACKは共通NACK形式とPDF該当節を併せて確認してください。予約バイトは、PDFで意味が定義されていない限り、独自解釈しないでください。

ACK、後続レスポンス、可変長データの解釈は、コマンド番号だけで固定せず、`../../RESPONSE_AND_NACK_MASTER.md` の起動時スナップショットに基づいてください。ROM・機種、アンテナID出力、TID付加、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM/FLASH設定の状態により、ACKのタイミングや応答データ長が変わります。

### 8.1 ACK/レスポンス例（成功時）

| 項目 | 内容 |
|---|---|
| 成功ACK例 | `02 00 30 01 18 03 4E 0D` |
| ACKデータ部の先頭 | `18h` |
| 注意 | タグメモリ操作は、Select/Query/Access/Write/Lock/Kill等の内部処理結果によりNACKになる場合があります。ここに示すHexは正常終了時のACK例であり、実行可否や対象タグ条件を省略してよいという意味ではありません。成功ACKだけでなく、NACKのエラーコード1/2を必ず解析してください。 |

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 18 44 00 00 00 00 00 00 00 00 03 9C 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

- アンテナID出力ON/OFFにより、レスポンスのアドレス位置がリーダライタIDまたは読み取りANT番号に変わります。
- 読取完了応答、アンテナ切替完了応答、キャリア検知応答のON/OFFで、後続ACKの有無が変わります。
- 設定変更またはタグメモリ変更後は、対応する読み取りコマンドで読戻し確認してください。


### 8.4 AI実装用レスポンス定義

この節は、生成AIや実装者がACK/レスポンス処理を固定文言ではなく、byte位置と設定依存で実装するための機械可読寄りの整理です。公式PDFの該当節を一次情報とし、この表は実装時のチェックリストとして使ってください。

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

#### 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| フレーム長不一致、`STX/ETX/CR/SUM`不正 | `INVALID_FRAME` | 破棄し、必要なら再同期する |
| 受信期限内に1フレームも来ない | `TIMEOUT` | timeoutとして処理し、NACKとは分ける |
| `CMD=31h` | `NACK` | 共通NACK表でエラーコードを読む |
| `CMD=30h` かつ `DATA[0]` が `18h` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 18h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` の後にタグ状態確認が必要 | `ACK_PENDING_TAG_VERIFY` | タグメモリ操作はACKだけで業務成功と断定しない |

対象識別子: コマンド `55h` / 詳細 `18h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は、原則として `18h` またはPDF該当節の応答識別子として扱います。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail/status` | 対象コマンドの詳細識別子または状態識別子 |
| 1.. | `payload` | PDF該当節の順序で読む。予約byteは独自解釈しない |

タグメモリ操作系は、ACKが通信成功を示しても、タグ上の最終状態確認が必要な場合があります。NACK時はUHF ICエラー詳細を必ず残してください。

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 18h` |
| 1 | `error_code_1` | FORMAT_ERROR、SUM_ERROR、LBT_ERROR、ANTENNA_ERROR、UHF_IC_ERRORなどの主エラー |
| 2 | `error_code_2` | `error_code_1=0Ah` のUHF ICエラー時に参照 |
| 3 | `error_code_3` | UHF_Encode / UHF_BlockWrite2 等でPDF定義がある場合のみ参照 |
| 4 | `error_code_4` | PDF定義がある場合のみ参照 |
| 5..9 | reserved | PDFで意味が定義されていない限り独自解釈しない |

判定: `CMD=31h` を受けた時点で `NACK`。`error_code_1` が0でも成功扱いにしないでください。

#### 最小疑似コード

```text
frame = read_next_frame(timeout)
if frame is None:
    return TIMEOUT
parsed = parse_common_frame(frame)
if parsed.invalid:
    return INVALID_FRAME
if parsed.cmd == 0x31:
    return parse_nack(parsed)
if parsed.cmd == 0x30:
    return parse_ack_payload(parsed, settings_snapshot)
if parsed.cmd == 0x6C:
    return RF_TAG_DATA_ASYNC_EVENT
return UNKNOWN_RESPONSE_REQUIRES_PDF_CHECK
```

#### 推奨パーサ出力

```json
{
  "frame_type": "ACK | NACK | RF_TAG_DATA | COMPLETION | ANT_SWITCH_COMPLETE | CARRIER_DETECTED | NO_RESPONSE | TIMEOUT | INVALID_FRAME",
  "command": "対象コマンド名",
  "address_role": "reader_id | antenna_id | unknown",
  "detail": "PDFで定義された詳細コマンドまたは応答種別",
  "data_length": 0,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### 設定スナップショット必須項目

実行前に、ROM/機種、物理アンテナ容量、接続OKアンテナ、現在ANT、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM/FLASH対象を取得し、この結果をパーサへ渡してください。
## 9. 実機確認

実機確認区分: `tag-memory-or-high-impact`

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
