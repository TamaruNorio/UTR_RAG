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
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "55_33_03_write_access_password.md"
  - "55_16_uhf_write.md"
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
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

対象領域のPasswordロックを設定・解除し、必要に応じてその状態をPermaLockで固定します。

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

```

### Lockの原典転記：対象領域と処理種別

<a id="lock-regions"></a>

[認証条件と恒久化](#lock-conditions)と併せて参照してください。

```text
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
```

### Lockの原典転記：認証条件と恒久化

<a id="lock-conditions"></a>

[対象領域と処理種別](#lock-regions)に対する説明です。p.227の訂正は[OPEN-014](../../SOURCE_REVIEW_STATUS.md)で保留中です。

```text
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
```

### Lockの原典転記：フラグ以降

```text



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

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 要求・応答の照合ポイント

PDF §7.5.6 p.278–282の補足です。DATAは0起点で、共通フレームのoffset 4から始まります。

### 8.1 非ゼロのAccessパスワードを事前に一致させる

p.278では、タグのReserved領域Word 02hから2 Wordと、リーダライタに設定したAccessパスワードが、非ゼロかつ一致することを要求しています。[Access設定](55_33_03_write_access_password.md)はリーダライタ側のRAM設定で、タグ側の値を変更しません。タグ側のパスワード設定は[Write](55_16_uhf_write.md)等の別操作です。Lock要求内にパスワード欄はありません。

対象タグはSelectとQueryの条件で1枚に絞ります。内部QueryのQは設定値によらず0です（p.64）。Q=0やACKだけでは対象の一意性を保証しません。

### 8.2 MaskとActionの配置

CMD=55h、LEN=04h、総11 byteです。DATA[0]=18h、DATA[1]=パラメータ1（P1）、DATA[2]=P2、DATA[3]=P3です。P3のbit0～3は0固定です。以下はp.279の表を、同じ対象・種別のMaskとActionが対になる形へ並べ直したものです。

#### Passwordロックの5組

| 対象 | 種別 | Mask位置 | Action位置 |
|---|---|---|---|
| TID | PasswordWrite | P1 bit1 | P3 bit7 |
| EPC | PasswordWrite | P1 bit3 | P2 bit1 |
| Access Password | PasswordRead/Write | P1 bit5 | P2 bit3 |
| Kill Password | PasswordRead/Write | P1 bit7 | P2 bit5 |
| User | PasswordWrite | P2 bit7 | P3 bit5 |

#### PermaLockの5組

| 対象 | 種別 | Mask位置 | Action位置 |
|---|---|---|---|
| TID | PermaLock | P1 bit0 | P3 bit6 |
| EPC | PermaLock | P1 bit2 | P2 bit0 |
| Access Password | PermaLock | P1 bit4 | P2 bit2 |
| Kill Password | PermaLock | P1 bit6 | P2 bit4 |
| User | PermaLock | P2 bit6 | P3 bit4 |

#### フラグの意味

Mask=0ならその対象・種別のActionを書き込まず、Actionが0でも1でも変更しません。Mask=1ならAction=1で設定、Action=0で解除を指定します。既に固定されたPermaLockはAction=0でも解除できません（p.281）。全領域へ一律のMaskを作るのではなく、要求された対象と処理種別だけを指定します。

p.282の例はUserのPasswordWriteだけを操作します。P1/P2/P3が00/80/20なら設定、00/80/00なら解除で、他の領域・PermaLockのMaskは0です。これらはPDF掲載パラメータの説明であり、対象条件を満たさない実機への送信許可ではありません。

### 8.3 ロックの範囲と恒久化

p.280の定義では、EPC・TID・UserのPasswordWriteは認証なしでもRead可能、Writeには認証が必要です。Access Password・Kill PasswordのPasswordRead/WriteはReadとWriteの両方に認証が必要です。タグ固有の領域の実装・読取り専用属性を、Lockコマンドで変更できるとは限りません。

同ページのPermaLockは、Lockの設定／解除状態を固定する処理です。Write Lock設定中の恒久化と、解除中の恒久化を区別します。前者はWrite不可のまま、後者はWrite可能なままLockを設定できなくなります。リーダライタのパスワード変更や再起動で恒久化を取り消せません。

p.227の包括的な「PermaLockなら読み書き不可」という記載の訂正は、[原典照合一覧](../../SOURCE_REVIEW_STATUS.md)のOPEN-014で確認中です。この節はp.280の具体的な説明を整理したもので、p.227の訂正文を確定したものではありません。

### 8.4 固定ACKとLock確認

成功ACKはCMD=30h、LEN=01h、DATA[0]=18h、総8 byteです。共通フレームを検査し、この3条件で要求と対応づけます。各領域のMask・Action・設定後の状態は返りません。ADRはリーダライタIDです。TID付加や自動読み取りの通知設定で、このACKの構造・有無を変えません。

p.281では、Lock直後に正しいAccessパスワードがリーダライタ側へ残っていると、Writeできる場合を説明しています。これを直ちにLock失敗と判断しません。不要になったAccess設定はゼロへ戻しますが、リーダライタ側のゼロ化はタグのLock解除ではありません。

以下は確認計画上の注意です。要求した領域・種別・Mask・Action、成功ACK、許可された範囲での認証条件別の確認を別々に記録します。タグメモリのRead結果に汎用のLock状態フィールドがあると仮定しません。状態確認のために新たな書込み・解除・恒久化を自動追加しません。

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
- [55_16_uhf_write](55_16_uhf_write.md)
- [55_30_uhf_set_select_param](55_30_uhf_set_select_param.md)
- [55_31_uhf_set_inventory_param](55_31_uhf_set_inventory_param.md)
- [RAM_FLASH_IMPACT_MATRIX](../../RAM_FLASH_IMPACT_MATRIX.md)
- [SOURCE_REVIEW_STATUS](../../SOURCE_REVIEW_STATUS.md)

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
