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
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "55_1a_uhf_block_write.md"
  - "4e_b4_flash_write.md"
  - "55_15_uhf_read.md"
  - "55_33_03_write_access_password.md"
  - "55_30_uhf_set_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
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
  - "specification-reference"
  - "uhf-block-write2"
---

# UHF_BlockWrite2（ブロック書き込み2）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_BlockWrite2** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.9`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `1Dh` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

1枚のタグへ最大124 WordをRF側BlockWriteで一括送信します。対応するデータ量はタグ仕様にも依存します。

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


```

### BlockWrite2の原典転記：方式比較とタグ対応

<a id="bw2-compatibility"></a>

[応答時間の注意](#bw2-timing)と併せて参照してください。

```text
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
```

### BlockWrite2の原典転記：応答時間と掲載チップ

<a id="bw2-timing"></a>

[方式比較とタグ対応](#bw2-compatibility)から続く注意です。「弊社」は原典の筆者を指し、本リポジトリでの実機試験結果ではありません。

```text
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
```

### BlockWrite2の原典転記：要求形式以降

```text



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

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

PDF §7.5.9 p.288–290の補足です。DATAは0起点で共通フレームoffset 4から始まります。

### 8.1 2 byteアドレスと1 byteのWord数

CMD=55h、LEN=5+2n、総フレーム長=12+2nです。nは書込みWord数で、最大124 Word（248 byte）。124 WordならLEN=FDh、総260 byteです。LENはDATAの長さであり、総フレームを255 byteまでに制限しません。

| DATA位置 | 長さ | 内容 |
|---|---:|---|
| 0 | 1 | 詳細1Dh |
| 1 | 1 | bit1..0: 00=Reserved、01=EPC/UII、10=TID、11=User。bit2..7は予約、通常0 |
| 2..3 | 2 | 開始Wordアドレス、上位byte・下位byteの順 |
| 4 | 1 | 書込みWord数n |
| 5.. | 2n | 書込みデータ |

BlockWriteの4 byteアドレス・2 byte Word数・RF側コマンド選択欄を流用しません。実データ長=2n、LEN=5+2nを照合します。n=0の扱いは当該節では未確認です。124 Wordはコマンドの上限で、タグ容量や一括書込み対応数を保証しません。

### 8.2 一括送信・タグ対応・時間

本コマンドはRF側BlockWriteでデータを一括送信します。p.288は、一部タグが2 Wordまたは3 Word以上のBlockWriteに未対応と説明しています。対応チップとして記載されるMB97R8110・Higgs ECも、本整備で実機確認した結果ではありません。

p.290のHiggsEC・User領域8 Wordの平均時間は、BlockWrite使用89ms、Write使用109ms、BlockWrite2使用64msです。同じ条件での掲載例であり、全タグの性能保証やホストtimeoutの設定値ではありません。RF側への一括送信から、原子的な更新や失敗時の巻戻しを推論しません。

#### RF側timeoutとホスト側timeout

p.288では、RF側BlockWriteの応答待ちをFLASHアドレス92（5Ch）で設定し、期限内に応答しないとリーダライタがNACKを返すと説明しています。p.344ではこのアドレスはROM Ver.2.030以降、初期値20msです。p.288には多数Wordでは設定可能範囲の20ms以内に応答しない場合があるとの注意があります。

この20msをUSB/COM・LAN/TCPのホスト受信期限へ流用しません。内部処理やリトライ（p.66）と通信時間は別です。ホストがNACKを受信した場合と、ホスト自身の待機期限切れは別の結果です。FLASHのtimeout設定変更は本コマンドと別操作で、適用ROM・設定範囲の確認なしに延長しません。

### 8.3 成功ACKは8 byte固定

成功ACKはCMD=30h、LEN=01h、DATA[0]=1Dh、総8 byteです。共通フレームの長さ・STX・ETX・CR・SUMを検査し、CMD・LEN・詳細を要求と対応づけます。bank・開始位置・処理Word数・結果データは返りません。

ADRはリーダライタIDです。タグの読取りデータを含まないこのACKへ、アンテナID出力による番号置換を一般化しません。TID付加や自動読み取り用の通知設定でACKの構造・有無を変えません。

### 8.4 対象・Access・変更後の確認

対象はSelect／Query条件で1枚に絞ります。内部Queryは設定Q値によらずQ=0ですが、一意性の保証ではありません（p.64）。リーダライタに非ゼロのAccessパスワードが設定されていればAccessを発行します（p.226）。[Access設定](55_33_03_write_access_password.md)はRAM設定で、タグのパスワード書換えとは別です。対象領域の容量・ロック・タグ固有の対応も確認します。

以下は運用上の注意です。ACK受信と期待値の読戻し一致を区別します。読取り可能な範囲は[Read](55_15_uhf_read.md)で確認できますが、同コマンドの上限は32 Wordなので、長い領域は範囲を分ける計画が必要です。変更箇所がSelectマスクに含まれる場合は変更後の対象同定も決め、失敗時に選別範囲を無条件に広げません。NACK・timeoutだけで未変更や自動的な巻戻しを保証せず、確認なしの再送をしません。

### 8.5 NACKにはコード3・4もある

共通NACKはCMD=31h、LEN=0Ah、総17 byteです。BlockWrite2のコード3はEncodeの「失敗した領域」を表す表とは異なります（p.316–318）。

| DATA位置 | フィールド | 解釈 |
|---|---|---|
| 0 | 詳細 | 1Dh。要求と対応づける |
| 1 | コード1 | p.317上段の共通エラー表 |
| 2 | コード2 | コード1=0Ahの場合にp.317下段の表を参照 |
| 3 | コード3 | BlockWrite2ではp.317上段の共通エラー表 |
| 4 | コード4 | コード3=0Ahの場合にp.317下段の表を参照 |
| 5..9 | 予約 | 意味を与えず、SUMには含める |

コード1・2とコード3・4の組を独立に解釈します。コード3=03hを「User領域で失敗」と解釈したり、コード3=0Ahの詳細をコード2だけから取得したりしません。成功Word数や失敗WordアドレスはこのNACKに定義されていません。[共通NACKマスタ](../../RESPONSE_AND_NACK_MASTER.md)の対応表に従い、コード1が0でもCMD=31hを成功に変更しません。

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

- [55_1a_uhf_block_write](55_1a_uhf_block_write.md)
- [4e_b4_flash_write](4e_b4_flash_write.md)
- [55_15_uhf_read](55_15_uhf_read.md)
- [55_33_03_write_access_password](55_33_03_write_access_password.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [SOURCE_REVIEW_STATUS](../../SOURCE_REVIEW_STATUS.md)
- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
