---
title: "UHF_Kill"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.5"
command_group: "rf_tag_communication"
command_name: "UHF_Kill"
command_byte: "55h"
detail_command: "17h"
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
  - "55_33_03_write_access_password.md"
  - "55_30_uhf_set_select_param.md"
  - "55_31_uhf_set_inventory_param.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../SOURCE_REVIEW_STATUS.md"
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
  - "uhf-kill"
---

# UHF_Kill（タグ無効化）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_Kill** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.5`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `17h` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

対象のRFタグを、以降のRFタグ通信コマンドへ応答しないKilled状態にします。元には戻せません。

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
| Accessパスワード確認 | あり（非ゼロ設定時のAccess発行条件。要求内はKill用） |
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

以下は、公式PDF `7.5.5` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.5   UHF_Kill
  RFタグをKill（無効化）するコマンドです。
  Kill（無効化）されたRFタグは、Killed状態に遷移し、全ての「RFタグ通信コマンド」に対して応
  答を返さなくなります。
    ※RFタグの状態遷移については、「4.1 RFタグの状態遷移」をご参照ください。

  ・RFタグをKill（無効化）するためには、RFタグのKill Password (Reserved領域のWordアドレス
   [00]hから2[Word])に[0000 0000]h以外を書き込んだ状態で本コマンドを実行し、RFタグのKill
   Passwordと、本コマンドのコマンドパラメータで指定するKill Passwordが、一致する必要があり
   ます。
  ・RFタグへ設定するKill Passwordは、[UHF_Write], [UHF_BlockWrite], [UHF_Encode]コマンド
   などを使用して事前に書き込みます。
  ・一度Killed状態となったRFタグは、元に戻すことはできません。

  ・本コマンドを実行すると、ISO18000-63 規格で規定された、[Select], [Query], [Kill]などのコマン
   ドを、リーダライタが自動的に順次実行します。
        ・リーダライタと RF タグ間で実行されるコマンドの詳細は、
                                     「3.10 RF タグ通信コマンド実行時
         のリーダライタの内部処理」をご参照ください。
        ・読み書き対象の RF タグが 1 枚となるように、あらかじめ[Select]コマンドのマスク条件や
         [Query]コマンドのパラメータを設定した状態で本コマンドを実行してください。
         複数の RF タグが応答を返す状態でコマンドを実行すると、意図しない RF タグに対して
         コマンドが実行されたり、コマンドの実行に失敗したりする可能性があります。


 ［コマンド］
 ラベル名 バイト数                                内容
  STX          1   02h
 アドレス          1   00h（「5.2 通信フォーマットの詳細」参照）
 コマンド          1   55h
 データ長          1   05h
               1   17h（詳細コマンド）
 データ部              Kill Password
               4
                     MSB ファーストでセットする
   ETX         1   03h
   SUM         1   SUM 値（「5.3 SUM の計算方法」参照）
    CR         1   0Dh


  ＜コマンドパラメータ＞
   ● Kill Password
       リーダライタからの[Kill]コマンドに設定するKill Passwordを指定します。
       RFタグをKill（無効化）するためには、RFタグのKill Password (Reserved領域のWordアド
       レス[00]hから2[Word])に書かれている内容と同じ内容を指定する必要があります。


［ACK レスポンス］
ラベル名 バイト数                                       内容
 STX          1      02h
アドレス          1      00h（「5.2 通信フォーマットの詳細」参照）
 ACK          1      30h
データ長          1      01h
データ部          1      17h（詳細コマンド）
 ETX          1      03h
 SUM          1      SUM 値（「5.3 SUM の計算方法」参照）
  CR          1      0Dh


［NACK レスポンス］
 「7.6 NACK レスポンスとエラーコード」参照。


［コマンド／レスポンス例］
       ● コマンド
          02 00 55 05 17 <PASSWORD_BYTES> 03 8A 0D
       ● レスポンス
          02 00 30 01 17 03 4D 0D
    ※Kill Password に[<PASSWORD_BYTES>]h を指定して[Kill]コマンドを実行し、
     Kill（無効化）に成功した場合
     →RF タグは ACK 応答を返した後、Killed 状態となります。
       Killed 状態となった RF タグは、以降の全ての RF タグ通信コマンドに対して応答を
       返さなくなります。
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

PDF §7.5.5 p.276–277の補足です。DATAは0起点で、共通フレームのoffset 4から始まります。

### 8.1 要求内のパスワードはKill用

CMD=55h、LEN=05h、総12 byteです。DATA[0]=17h、DATA[1..4]はKill Passwordの4 byteで、MSB先行です。MemBank、Wordアドレス、Accessパスワード、予約byteの追加欄はありません。

タグのReserved領域Word 00h～01hに非ゼロのKill Passwordが事前に設定され、要求内のKill Passwordと一致することが条件です。ゼロを無認証実行や確認用の指定として扱いません。この要求はタグのKill Passwordを書き換えるコマンドではありません。

### 8.2 Access条件との区別

p.226のAccess設定対象にはUHF_Killも含まれ、リーダライタのAccessパスワードが非ゼロならAccessを発行する仕様です。p.276の「Select、Query、Killなど」という内部処理の列挙はAccessの発行を否定していません。

`requires_access_password: true`は、このリーダライタ側設定条件の確認を表します。Kill要求へAccessパスワードを入れる意味でも、Killのために常に非ゼロのAccess設定を要求する意味でもありません。[Access設定カード](55_33_03_write_access_password.md)を併読し、Kill用の4 byteと区別します。この整理はPDFによるもので、実機試験結果ではありません。

### 8.3 対象は1枚、成功ACKは8 byte

SelectとQueryの条件で対象を1枚に絞ります。Qは設定値によらず0ですが（p.64）、対象の一意性を保証しません。複数タグが応答すると別タグへの実行や失敗の可能性があります。

成功ACKはCMD=30h、LEN=01h、DATA[0]=17h、総8 byteです。共通フレームを検査した後にこの3条件を照合します。タグID・パスワード・状態byteは返りません。ADRはリーダライタIDで、タグの読取りデータを含まないACKへアンテナ番号への置換を一般化しません。自動読み取り用の通知設定やTID付加でACKを変更しません。

### 8.4 成功後は読戻しできない

p.277では、RFタグがACKを返した後にKilled状態へ遷移し、その後のRFタグ通信コマンドには応答しなくなります。ホスト側では定義された成功ACKを記録します。一度Killed状態となったタグを元へ戻すことはできません（p.276）。

従来の汎用説明にあった「ACK後にタグメモリを読戻す」は適用できません。一方で、後続の無応答だけでは、Kill済み・圏外・選別条件不一致・通信障害を区別できません。以下は確認計画上の注意として、対象の事前同定、要求とACKの対応、その後の観測を分けます。Killの再実行を成功確認に使いません。

### 8.5 NACK・timeoutと要求の対応

共通NACKはCMD=31h、LEN=0Ah、総17 byteです。DATA[0]の詳細コマンドで要求と対応づけ、DATA[1]をエラーコード1として読みます。コード1=0Ahの場合のみDATA[2]のエラーコード2を参照します。本コマンドへEncode／BlockWrite2用の追加コードを転用しません。予約byteもSUMに含めます。

[共通NACKマスタ](../../RESPONSE_AND_NACK_MASTER.md)と[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)を参照してください。保守者訂正済みの[81h: ハンドル取得失敗]と[04h: メモリロック]はコード2です。各値がどの条件で返るかを推測で追加せず、NACKを正常なタグ0枚に読み替えません。

以下は運用上の注意です。ACK・NACK・timeoutと、その後に確認できた状態を分けて記録します。timeoutで変更前の状態を保証せず、自動再試行や選別条件の拡大をしません。RF通信の内部リトライとホスト側の再送は別で、PDF p.66ではリトライ設定0でも内部再試行がある場合を説明しています。

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

- [55_33_03_write_access_password](55_33_03_write_access_password.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)
- [SOURCE_REVIEW_STATUS](../../SOURCE_REVIEW_STATUS.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
