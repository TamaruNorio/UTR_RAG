---
title: "UHF_CheckAntenna"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.5"
command_group: "reader_control"
command_name: "UHF_CheckAntenna"
command_byte: "55h"
detail_command: "44h"
subcommand: null
operation_profile: "rf-read"
operation_level: "RF diagnostic"
rf_emission: true
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: true
requires_tag: false
requires_access_password: false
requires_parameters: false
verification_status: "REAL_DEVICE_VERIFIED_WITH_NOTES"
result_status: "REAL_DEVICE_PASS_WITH_NOTES"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../PARAMETER_CONFIRMATION_GUIDE.md"
  - "../../AI_IMPLEMENTATION_GUARDRAILS.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-control"
  - "rf-emission"
  - "requires-antenna"
  - "pass-with-notes"
  - "uhf-check-antenna"
---

# UHF_CheckAntenna（アンテナ確認）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_CheckAntenna** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.5`
- コマンド分類: リーダライタ制御
- 確認区分: `rf-read`
- 操作レベル: RF diagnostic
- コマンドバイト: `55h` / 詳細コマンド: `44h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_CheckAntenna** です。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

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
| パラメータ確認 | なし |
| 明示許可 | 不要または通常不要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. 読み取り専用か、設定変更か、タグメモリ操作かを分類する。
4. 実機送信が必要な場合は、接続先、タイムアウト、ログ保存先、停止条件を決める。
5. 周波数、送信出力、アンテナ設定、FLASH、タグメモリに影響する場合は、事前承認を取る。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.3.5` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.3.5   UHF_CheckAntenna
  アンテナの接続確認用のコマンドです。

  ［コマンド］
 ラベル名 バイト数                                 内      容
  STX         1    02h
 アドレス         1    00h（「5.2 通信フォーマットの詳細」参照）
 コマンド         1    55h
 データ長         1    02h
              1    44h（詳細コマンド）
                   アンテナ番号
                   UTR-S201 の場合      UTR-SUN02-4CH     UTR-SUN02V-8CH
                   UTR-SHR201 の場合    の場合               の場合

                   00h : ANT0        00h : ANT0        UTR-SUN02-8CH
                                     01h : ANT1        の場合
                                     02h : ANT2
 データ部                                                  00h : ANT1
              1                      03h : ANT3
                                                       01h : ANT2
                                                       02h : ANT3
                                                       03h : ANT4
                                                       04h : ANT5
                                                       05h : ANT6
                                                       06h : ANT7
                                                       07h : ANT8
   ETX        1    03h
   SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
    CR        1    0Dh


 ［ACK レスポンス］
ラベル名 バイト数                                内      容
 STX        1    02h
アドレス        1    00h（「5.2 通信フォーマットの詳細」参照）
 ACK        1    30h（ACK）
データ長        1    03h
            1    44h（詳細コマンド）
                 アンテナ番号
                 UTR-S201 の場合      UTR-SUN02-4CH     UTR-SUN02V-8CH
                 UTR-SHR201 の場合    の場合               の場合

                 00h : ANT0        00h : ANT0        UTR-SUN02-8CH
                                   01h : ANT1        の場合
                                   02h : ANT2
                                                     00h : ANT1
            1                      03h : ANT3
                                                     01h : ANT2
データ部                                                 02h : ANT3
                                                     03h : ANT4
                                                     04h : ANT5
                                                     05h : ANT6
                                                     06h : ANT7
                                                     07h : ANT8
                 接続情報
                   00h    ：アンテナの接続 OK
            1
                   01h    ：アンテナの接続エラー
                   02h    ：アンテナがパラメータ異常
 ETX        1    03h
 SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
  CR        1    0Dh


  ● 接続情報
     アンテナ番号で指定した出力端子のアンテナの断線確認を実施し、その接続状態により
     以下のレスポンスが返ります。
      [00h: アンテナの接続 OK]
        適切にアンテナが接続されており、アンテナのマッチングが良好の場合
      [01h: アンテナの接続エラー]
        断線確認した出力端子にアンテナが接続されていない場合や、接続されたアンテナのマッ
        チングが極端にずれている場合
          ※アンテナ周囲の誘電体(水分や人体を含む)や金属物等の影響により、アンテナの特性に
            影響を与える場合があります。アンテナの特性が極端に悪くなった場合、リーダライタ
            は、アンテナの断線を検知する場合があります。
            アンテナは、周囲環境の影響を受けない場所に設置してください。

      [02h: アンテナがパラメータ異常]
        存在しないアンテナ番号を選択した場合
        ・機種により、アンテナポート数が異なります。機種ごとのアンテナポート数は下表の通り
          です。
                                            アンテナ         備考
           製品の種類              製品型式
                                            ポート数
                           UTR-SUN02-4CH     4     ANT0～ANT3 が設定可能
            据置型            UTR-SUN02V-8CH    8     ANT1～ANT8 が設定可能
                           UTR-SUN02-8CH     8     ANT1～ANT8 が設定可能
        基板モジュール型              UTR-S201       1      ANT0 のみ設定可能
           ハンディ型             UTR-SHR201      1      ANT0 のみ設定可能


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］
   • コマンド
      02 00 55 02 44 00 03 A0 0D
   • レスポンス
      02 00 30 03 44 00 00 03 7C 0D
              ANT0 ↑ ↑アンテナの接続 OK
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

### 8.1 ACK/レスポンス例（RF処理成功時）

| 項目 | 内容 |
|---|---|
| 成功ACK構造例 | `02 ADR 30 01 44 <RF処理結果...> 03 7A 0D` |
| ACK/応答データ部の先頭 | `44h` |
| RFタグ応答 | コマンドにより、ACKとは別にRFタグデータ、読取完了ACK、またはエラーNACKが返ります。 |

RF系では1送信1応答に固定しません。タグ応答、完了応答、NACK、timeoutを同じ受信ループで分類してください。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 44 44 00 00 00 00 00 00 00 00 03 C8 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

- アンテナID出力ON/OFFにより、レスポンスのアドレス位置がリーダライタIDまたは読み取りANT番号に変わります。
- 読取完了応答、アンテナ切替完了応答、キャリア検知応答のON/OFFで、後続ACKの有無が変わります。


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
| `CMD=30h` かつ `DATA[0]=44h` | `ACK` | 対象コマンド `55h 44h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期タグ応答候補。要求コマンドのACKと混同しない |
| `CMD=30h` かつ `DATA[0]=10h` `DATA[1]=02h` | `CARRIER_DETECTED` | キャリア検知応答ON時のみイベントとして扱う |

対象識別子: コマンド `55h` / 詳細 `44h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は、原則として `44h` またはPDF該当節の応答識別子として扱います。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail/status` | 対象コマンドの詳細識別子または状態識別子 |
| 1.. | `payload` | PDF該当節の順序で読む。予約byteは独自解釈しない |

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 44h` |
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

実機確認区分: `rf-read`

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
- `../../RF_SAFETY_AND_CARRIER_RULES.md`
- `../../PARAMETER_CONFIRMATION_GUIDE.md`
- `../../AI_IMPLEMENTATION_GUARDRAILS.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
