---
title: "UHF_BlockWrite2"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.9"
command_group: "rf_tag_communication"
command_name: "UHF_BlockWrite2"
command_byte: "55h"
detail_command: "1Dh"
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
---

# UHF_BlockWrite2（ブロック書き込み2）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_BlockWrite2** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.9`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `1Dh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_BlockWrite2** です。

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

以下は、公式PDF `7.5.9` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.9   UHF_BlockWrite2
  RFタグに最大124[Word]のデータを一括書き込みするためのコマンドです。
  RFタグに大容量データを書き込む場合に、本コマンドを使用することで、[UHF_BlockWrite]コマ
  ンドと比較して処理時間を短くすることができます。

  本コマンドを実行すると、ISO18000-63 規格で規定された、[Select], [Query], [Access],
  [BlockWrite]などのコマンドを、リーダライタが自動的に順次実行します。
    ※リーダライタと RF タグ間で実行されるコマンドの詳細は、
                                 「3.10 RF タグ通信コマンド実行時の
     リーダライタの内部処理」をご参照ください。
    ※読み書き対象の RF タグが 1 枚となるように、あらかじめ[Select]コマンドのマスク条件や
     [Query]コマンドのパラメータを設定した状態で本コマンドを実行してください。
     複数の RF タグが応答を返す状態でコマンドを実行すると、意図しない RF タグに対して
     コマンドが実行されたり、コマンドの実行に失敗したりする可能性があります。
    ※リーダライタの Access パスワードに[0000 0000]h 以外が設定されている場合には、書き込みす
     る MemBank によらず、必ず、[Access]コマンドが発行されます。


  ＜UHF_BlockWriteコマンドとUHF_BlockWrite2コマンドの違い＞
    ・[UHF_BlockWrite]コマンドは、上位機器から指定した最大32[Word]のデータを、
     1[Word]単位で、RFタグにBlockWriteコマンドまたはWriteコマンドで送信します。
    ・[UHF_BlockWrite2]コマンドは、上位機器から指定した最大124[Word]のデータを、
     一括で、RFタグにBlockWriteコマンドを送信します。
        ・BlockWrite コマンドは、ISO18000-63 では RF タグのオプションコマンドのため、一部の
         RF タグでは対応していません。詳細は「4.2.7 RF タグオプションコマンド対応表」または
         使用する RF タグ Chip のデータシートを参照ください。
        ・一部のRFタグでは、2[Word]または3[Word]以上のBlockWriteコマンドに対応していないた
         め、本コマンドを使用しての書き込みができません。
         詳細は、使用するRFタグのデータシートを参照するか、あらかじめ書き込みの可否および
         書き込み精度の動作確認をおこなったうえでご使用ください。
        ・一度に書き込みするデータ量が大きいため、RFタグからのレスポンスが返るタイミング
         が、他のコマンドと比較して遅くなる傾向があります。本コマンドを実行した際の
         BlockWriteコマンドのタイムアウト時間は、FLASHアドレス92([5C]h)に設定していま
         す。指定時間以内にRFタグからの応答が返らない場合、リーダライタはNACK応答を返し
         ます。
        ※弊社にて動作確認しているRFタグのChip：
          Fujitsu社製 MB97R8110、Alien社製 Higgs EC
             ※書き込みWord数が多い場合、タイムアウト時間の設定可能範囲の20[msec]以内に
              RFタグからの応答が返らないことがありますので、必ず実機で検証を実施してか
              らご使用ください。


［コマンド］
ラベル名 バイト数                            内容
 STX   1          02h
アドレス   1          00h（「5.2 通信フォーマットの詳細」参照）
コマンド   1          55h
データ長   1          05h+（書き込み Word 数×2）
            1     1Dh（詳細コマンド）
                  パラメータ 1
                          MemBank ※左側が上位 bit
                         00   ：Reserved
                  bit0
            1            01   ：EPC(UII)
                  bit1
                         10   ：TID
                         11   ：User
                  bit2-7 将来拡張のための予約（通常は 0）
データ部
                  書き込み開始 Word アドレス
                    メモリ上の書き込み開始位置（Word 単位）
            2
                    1 バイト目：上位バイト（MSB）
                    2 バイト目：下位バイト（LSB）
           1      書き込み Word 数
         書き込み
         Word 数   書き込みデータ（最大 124[Word]）
           ×2
 ETX       1      03h
 SUM       1      SUM 値（「5.3 SUM の計算方法」参照）
  CR       1      0Dh


＜コマンドパラメータ＞
● MemBank
   書き込むメモリ領域を指定します。
   詳細は、  「4.2RF タグのメモリ構造」の項を参照ください。

● 書き込み開始Wordアドレス
   指定した MemBank 上の書き込み開始位置（Word アドレス）を指定します。

● 書き込み Word 数
   書き込むメモリのサイズを Word 長（2 [byte]単位）で指定します。

● 書き込みデータ
   書き込むデータを指定します。


［ACK レスポンス］
ラベル名 バイト数                                            内容
 STX          1      02h
アドレス          1      00h（「5.2 通信フォーマットの詳細」参照）
 ACK          1      30h
データ長          1      01h
データ部          1      1Dh（詳細コマンド）
 ETX          1      03h
 SUM          1      SUM 値（「5.3 SUM の計算方法」参照）
  CR          1      0Dh


［NACK レスポンス］
 「7.6 NACK レスポンスとエラーコード」参照。


［コマンド／レスポンス例］
    (例) UHF_BlockWrite2 コマンドを使用して、Alien 社製 HiggsEC の Chip を搭載する
        RF タグに書き込む場合
         データ種類                           数値／パラメータ                   コマンド列
         MemBank                         11: User                   03
         書き込み Word 開始アドレス                0                          00 00
         書き込み Word 数                     8                          08
         書き込みデータ                         0101 0202 0303 0404        同左
                                         0505 0606 0707 0808
    • コマンド
      02 00 55 15 1D 03 00 00 08 01 01 02 02 03 03 04 04 05 05 06 06 07 07 08 08 03 DF 0D
    • レスポンス
      02 00 30 01 1D 03 53 0D


［UHF_BlockWrite2 コマンドによる書き込み時間の短縮例］
    ・Alien 社製 HiggsEC の Chip を搭載する RF タグに対して、User 領域の Word アドレス
     [00]h から 8[Word]の書き込みを以下の条件で実行し、処理時間を計測しました。
       (1) [UHF_BlockWrite]コマンドを、[BlockWrite コマンド:使用する]の設定で実行
             → BlockWrite コマンドが 1[Word]単位で 8 回実行されます。
             → 平均実行時間：89[msec]
       (2) [UHF_BlockWrite]コマンドを、[BlockWrite コマンド:使用しない]の設定で実行
             → Write コマンドが 1[Word]単位で 8 回実行されます。
             → 平均実行時間：109[msec]
       (3) [UHF_BlockWrite2]コマンドを使用
             → BlockWrite コマンドが 8[Word]一括送信で 1 回実行されます。
             → 平均実行時間：64[msec]
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
| 成功ACK例 | `02 00 30 01 1D 03 53 0D` |
| ACKデータ部の先頭 | `1Dh` |
| 注意 | タグメモリ操作は、Select/Query/Access/Write/Lock/Kill等の内部処理結果によりNACKになる場合があります。ここに示すHexは正常終了時のACK例であり、実行可否や対象タグ条件を省略してよいという意味ではありません。成功ACKだけでなく、NACKのエラーコード1/2を必ず解析してください。 |

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 1D 44 00 00 00 00 00 00 00 00 03 A1 0D` |
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
| `CMD=30h` かつ `DATA[0]` が `1Dh` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 1Dh` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` の後にタグ状態確認が必要 | `ACK_PENDING_TAG_VERIFY` | タグメモリ操作はACKだけで業務成功と断定しない |

対象識別子: コマンド `55h` / 詳細 `1Dh` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は、原則として `1Dh` またはPDF該当節の応答識別子として扱います。

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
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 1Dh` |
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
