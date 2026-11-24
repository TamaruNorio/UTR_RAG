---
title: "Accessパスワードの書き込み"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.23"
command_group: "reader_setting"
command_name: "Accessパスワードの書き込み"
command_byte: "55h"
detail_command: "33h"
subcommand: "03h"
operation_profile: "settings-change"
operation_level: "write/configuration"
rf_emission: false
write_operation: true
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: true
requires_parameters: true
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "55_15_uhf_read.md"
  - "55_16_uhf_write.md"
  - "55_17_uhf_kill.md"
  - "55_18_uhf_lock.md"
  - "55_1e_uhf_encode.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../SOURCE_REVIEW_STATUS.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-setting"
  - "write-operation"
  - "access-password"
  - "specification-reference"
  - "write-access-password"
---

# Accessパスワードの書き込み

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **Accessパスワードの書き込み** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.23`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `33h` / サブコマンド: `03h`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

リーダライタのRAMに、後続のRFタグ認証で使用するAccessパスワードを設定します。

詳細なフィールド定義、データ長、レスポンス形式は公式PDFを一次情報として確認してください。このカードは、公式PDFを置き換えるものではなく、AIに実装やレビューを依頼するときの補助資料です。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | あり |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | なし |
| タグ条件確認 | なし |
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

以下は、公式PDF `7.4.23` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.23 Access パスワードの書き込み
 本コマンドは、リーダライタに Access パスワードを設定するコマンドです。
  ※RF タグに Access Password を書き込むためのコマンドではありません。

 リーダライタに[0000 0000]h 以外のパスワードが設定された状態で、以下の「RF タグ通信コマンド」
 を実行すると、RF タグに対して[Access]コマンドが発行されます。
 パスワードが一致して認証に成功すると、ロック設定された RF タグの MemBank への読み書きが可
 能になります。
  ・[UHF_Read], [UHF_Write], [UHF_Kill], [UHF_Lock], [UHF_BlockWrite]
  ・[UHF_BlockErase], [UHF_BlockWrite2], [UHF_Encode]

  ［コマンド］
 ラベル名 バイト数                            内容
  STX       1    02h
 アドレス       1    00h（「5.2 通信フォーマットの詳細」参照）
 コマンド       1    55h
 データ長       1    07h
            1    33h（詳細コマンド）
            1    03h（詳細サブコマンド）
 データ部       1    将来拡張のための予約（通常は 00h）
                 Access パスワード
            4
                   MSB ファーストでセットする
  ETX       1    03h
  SUM       1    SUM 値（「5.3 SUM の計算方法」参照）
   CR       1    0Dh
 ※本コマンドは「コマンドモード用パラメータ」(RAM 値)です。FLASH へは書き込まれませんので、
  [リスタート]コマンドを実行したり、リーダライタの電源を OFF→ON したりすると、リーダライ
  タの Access パスワードは[0000 0000]h に戻ります。
 ※本コマンドを使用して、RF タグに Access パスワードを書き込むことはできません。
  RF タグに Access パスワードを書き込む際は、[8.5 RF タグにパスワードを書き込む]をご参照く
  ださい。
 ※セキュリティの観点から、リーダライタに書き込んだ Access パスワードは、読み取りすることは
  できません。

 ＜Access コマンドに関する注意事項＞
  ・Access コマンドは ISO18000-63 のオプションコマンドのため、一部の RF タグでは対応してい
    ません。そのため、リーダライタに Access パスワードを設定すると、Access コマンドに対応し
    ていない RF タグへのデータの読み書きができなくなります。
    Access コマンドに対応している RF タグの詳細は「4.2.7 RF タグオプションコマンド対応表」
    または使用する RF タグのデータシートを参照ください。

  ・Access コマンドの発行が必要なくなった時点で、必ず[0000 0000]h に戻すようにしてください。
   [0000 0000]h にしない限り、パスワードでロックされた RF タグに対してアクセス可能なままの
   状態となりますので、ご注意ください。
   特に、[UHF_Lock]コマンドや[UHF_Encode]コマンドで[Password Lock]を設定した直後は、リ
   ーダライタに RF タグと同一の Access パスワードが書き込まれていますので、Lock 設定した直
   後でも読み書き可能な状態となります。


  ・[PermaLock]状態が設定された RF タグに対しては、Access パスワードが一致した場合において
   も、読み書きすることはできません。
   [PasswordLock]状態の RF タグに対してのみ読み書きが可能です。

  ・[UHF_InventoryRead]コマンド、または、「UHF 連続インベントリリードモード」は、
   Access コマンドを発行せずに RF タグの「指定 MemBank」の読み取りをおこないます。
   そのため、読み取りする範囲が Password Read Lock されている場合は、読み取りすることが
   できず、読み取りのレスポンスが返りません。Password Read Lock された領域を読み取りする
   場合には、[UHF_Read]コマンドをご使用ください。

 ［ACK レスポンス］
ラベル名 バイト数                                          内容
 STX         1      02h
アドレス         1      00h（「5.2 通信フォーマットの詳細」参照）
コマンド         1      30h（ACK）
データ長         1      03h
             1      33h（詳細コマンド）
データ部         1      03h（詳細サブコマンド）
             1      将来拡張のための予約（通常は 00h）
 ETX         1      03h
 SUM         1      SUM 値（「5.3 SUM の計算方法」参照）
  CR         1      0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。


  ［コマンド／レスポンス例］

    (例) 以下のパラメータを書き込む場合 (Access パスワードに[AB CD 12 34]h を書き込む)
             データ種類    数値／パラメータ            コマンド列
       Access パスワード AB CD 12 34      AB CD 12 34

    • コマンド
       02 00 55 07 33 03 00 AB CD 12 34 03 55 0D
    • レスポンス
       02 00 30 03 33 03 00 03 6E 0D
```

## 7. コマンド形式の扱い

コマンド形式は、共通フレームとPDF該当節のフィールド定義に従って実装してください。

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

PDF §7.4.23 p.226–227の補足です。DATAは0起点で、共通フレームのoffset 4から始まります。

### 8.1 リーダライタに設定する4 byte

CMD=55h、LEN=07h、総14 byteです。

| DATA位置 | 長さ | 内容 |
|---|---:|---|
| 0 | 1 | 詳細33h |
| 1 | 1 | サブ03h |
| 2 | 1 | 予約、通常00h。RAM／FLASHのパラメータ種類ではない |
| 3..6 | 4 | Accessパスワード、MSB先行 |

設定先はリーダライタのコマンドモード用RAMです。DATA[2]へ02hを入れてFLASH保存する仕様ではありません。リスタート・電源再投入でゼロへ戻り、値は読戻せません。タグに書き込まれているパスワードやロック状態は、この設定・ゼロ化・リーダライタ再起動によって書き換わりません。

### 8.2 固定ACKと確認できる範囲

成功ACKはCMD=30h、LEN=03h、総10 byteです。

| DATA位置 | 内容 |
|---|---|
| 0 | 詳細33h |
| 1 | サブ03h |
| 2 | 予約、通常00h。設定値のechoやRAM／FLASH種類ではない |

共通フレームの長さ・STX・ETX・CR・SUMを検査し、CMD・LEN・詳細・サブを照合します。DATA[2]は予約として扱い、独自の状態を割り当てません。ACKにはパスワードが返らず、タグ認証成功も示しません。本コマンド自体はRF送信をせず、タグがなくてもリーダライタの設定操作として扱います。

p.227の掲載例も、リーダライタの設定成功を示す例です。存在しない読取りコマンドで確認する手順や、試しのLock／Killで設定を検査する手順を追加しません。

### 8.3 AccessパスワードとKillパスワード

| 設定・用途 | 格納先／指定先 | 本コマンドとの違い |
|---|---|---|
| リーダライタのAccessパスワード | 本コマンドのRAM設定、4 byte | タグとの認証に使用する値 |
| タグのAccess Password | ReservedのWord 02h～03h | タグメモリ書込みで設定する別の値 |
| タグのKill Password | ReservedのWord 00h～01h | Kill用。Accessパスワードで代用しない |

タグ内の位置は§4.2.1 p.84です。タグのパスワードを変更する操作は、対象と許可範囲を明示した[Write](55_16_uhf_write.md)等の別工程です。本コマンドのACKだけでタグ側も同じ値へ更新されたと判断しません。

### 8.4 後続コマンドへの影響

p.226では、非ゼロ設定時にAccessを発行する対象としてRead、Write、Kill、Lock、BlockWrite、BlockErase、BlockWrite2、Encodeを列挙しています。[Kill](55_17_uhf_kill.md)の要求内パスワードはKill用であり、このAccess設定とは別です。[Lock](55_18_uhf_lock.md)はp.278に両者のAccessパスワードが非ゼロかつ一致する条件があります。

Accessに未対応のタグでは、非ゼロ設定が後続の読み書きを妨げる場合があります。必要がなくなったらリーダライタ側をゼロへ戻す運用を決めます。Password Lock直後でも正しいAccess設定が残っていれば読み書きできる場合があり、それだけでLock失敗とは判断しません。

InventoryReadとUHF連続インベントリリードモードはAccessを発行しません（p.227）。Password Read Lock領域を読む場合は[Read](55_15_uhf_read.md)の条件を確認します。

p.227の「PermaLockなら読み書き不可」という包括的な記述と、p.280の状態別説明との関係は[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)のOPEN-014で保守者に確認中です。p.227の訂正本文は未確定で、原典転記を保持します。

#### Encodeの個別条件

[Encode](55_1e_uhf_encode.md)はp.297–299でbankごとのAccess発行指定と、Lock時の認証条件を定義しています。p.226の列挙だけから、全bankへ無条件に同じ認証を発行する手順にしません。p.295–296の保持設定とReserved書込みの成否によって、終了時のリーダ側Access設定も変わります。例2の不一致とゼロ化前の認証説明はOPEN-017／018で確認待ちです。

### 8.5 NACK・timeout・秘密値の管理

共通NACKはCMD=31h、LEN=0Ah、総17 byte、DATA[0]=33hで要求と対応づけます。サブ03hはNACKに返りません。DATA[1]はサブではなくエラーコード1であり、コード1=0Ahの場合のみDATA[2]をコード2として解釈します。RFタグの認証エラーと、リーダライタへの設定要求の失敗を混同しません。

受信期限までに応答がなければtimeoutです。読戻しができないため、設定値を確認できたと記録せず、許可された設定元から再設定するかを判断します。実パスワードを含む送信フレームは公開ログへ残しません。設定成功、後続タグ認証、終了時のゼロ化は別々に記録します。

## 9. 実機確認

実機確認区分: `settings-change`

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

- [55_15_uhf_read](55_15_uhf_read.md)
- [55_16_uhf_write](55_16_uhf_write.md)
- [55_17_uhf_kill](55_17_uhf_kill.md)
- [55_18_uhf_lock](55_18_uhf_lock.md)
- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)
- [SOURCE_REVIEW_STATUS](../../SOURCE_REVIEW_STATUS.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
