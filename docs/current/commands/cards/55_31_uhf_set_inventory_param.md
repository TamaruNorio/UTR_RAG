---
title: "UHF_SetInventoryParam"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.4.18"
command_group: "reader_setting"
command_name: "UHF_SetInventoryParam"
command_byte: "55h"
detail_command: "31h"
subcommand: null
operation_profile: "settings-change"
operation_level: "write/configuration"
rf_emission: false
write_operation: true
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
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
  - "reader-setting"
  - "write-operation"
  - "pass-with-notes"
---

# UHF_SetInventoryParam（Inventory条件設定）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_SetInventoryParam** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.4.18`
- コマンド分類: リーダライタ設定
- 確認区分: `settings-change`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `31h` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_SetInventoryParam** です。

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
| Accessパスワード確認 | なし |
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

以下は、公式PDF `7.4.18` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.4.18 UHF_SetInventoryParam
 「コマンドモード」、「UHF連続インベントリモード」、および「UHF連続インベントリリードモ
 ード」のインベントリ処理におけるパラメータの設定をおこなうコマンドです。


  ［コマンド］
 ラベル名 バイト数                               内容
  STX        1     02h
 アドレス        1     00h（「5.2 通信フォーマットの詳細」参照）
 コマンド        1     55h
 データ長        1     0Bh
             1     31h（詳細コマンド）
                   パラメータ種類 ※1
                     00h     ：コマンドモード用パラメータ
             1
                     01h     ：自動読み取りモード用パラメータ
                     02h     ：FLASH データ
                   パラメータ 1
                          Select コマンドの使用
                   bit0   0         ：使用しない
                          1         ：使用する ［初期値］
                          Q 値の自動 UP/DOWN 機能
 データ部              bit1   0         ：使用しない
                          1         ：使用する ［初期値］
                          アンチコリジョン機能
             1
                   bit2   0         ：使用しない
                          1         ：使用する ［初期値］
                          Q 値の開始値
                   bit3-6 0～15 ［初期値：3(0011b)］
                          ※bit3 を LSB とする 4[bit]の数値
                          Inventory の Target
                   bit7   0         ：A ［初期値］
                          1         ：B
   （次ページへ続く）


  （前ページからの続き）

ラベル名     バイト数                              内容
                 パラメータ 2
                      Session 値 ※左側が上位 bit
                      00       ：S0 ［初期値］
                 bit0
                      01       ：S1
                 bit1
                      10       ：S2
                      11       ：S3
                      Sel 値 ※左側が上位 bit
                      00       ：ALL
                 bit2
                      01       ：ALL
                 bit3
                      10       ：^SL
                      11       ：SL ［初期値］
            1
                           TRext 値
                 bit4      0     ：No pilot tone（未サポート）
                           1     ：Use pilot tone［初期値］
データ部                       M 値 ※左側が上位 bit
                           00    ：M1 （未サポート）
                 bit5
                           01        ：M2 （未サポート）
                 bit6
                           10        ：M4 ［初期値］
                           11        ：M8 （未サポート）
                           DR 値
                 bit7   0        ：8 （未サポート）
                        1        ：64/3 ［初期値］
                 パラメータ 3
                        Q 値の最小値
                 bit0-3 0～15 ［初期値：1 (0001b)］
            1           ※bit0 を LSB とする 4[bit]の数値
                        Q 値の最大値
                 bit4-7 0～15 ［初期値：8 (1000b)］
                        ※bit4 を LSB とする 4[bit]の数値
  （次ページへ続く）


  （前ページからの続き）

ラベル名     バイト数                          内容
                 パラメータ 4
                       MemBank ※左側が上位 bit
                       00     ：Reserved
                 bit0
                       01     ：EPC(UII)
                 bit1
                       10     ：TID［初期値］
            1
                       11     ：User
                       TID 付加
データ部             bit2   0     ：付加しない［初期値］
                        1     ：付加する
                 bit3-7 将来拡張のための予約（通常は     0）
                 読み取り開始 Word アドレス    初期値は[00 00 00 00]h
            4    RF タグのメモリ上の読み取り開始位置（Word 単位）
                 ※MSB ファーストで指定
                 読み取り Word 数  初期値は 2 (02h)
            1
                 読み取りする Word 数（1～32）
 ETX        1    03h
 SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
  CR        1    0Dh
※1：パラメータ種類の詳細は「3.12.1 パラメータ種類」をご参照ください。


  ● Select コマンドの使用 （FLASH 初期値：使用する）
    RF タグ読み取り時の Inventory 処理において、[Query]コマンド実行前に[Select]コマンドを発
    行するかどうかを指定します。
    アンテナの読み取り範囲内にある、読み取り対象以外の RF タグを除外する際に使用します。読
    み取り対象の RF タグのエンコードの方法を事前に決めて運用する必要があります。
    マスク条件を指定して[Select]コマンドを RF タグに対して実行すると、RF タグはマスク条件へ
    の[一致]／[不一致]により、RF タグ内部の「Inventoried フラグ」または「SL フラグ」の状態を
    遷移させます。
    その後、読み取りの対象フラグとフラグの状態を指定して[Query]コマンドを実行することで、
    対象の RF タグのみを読み取りすることができます。
    ・[使用する]
     リーダライタは、[Query]コマンド実行前に[Select]コマンドを発行します。
     Select コマンドのパラメータは、[UHF_SetSelectParam]コマンドで設定した内容が反映さ
     れます。
    ・[使用しない]
     リーダライタは、[Query]コマンド実行前に[Select]コマンドを発行しません。


  ● Q 値の自動 UP/DOWN 機能 （FLASH 初期値：使用する）
    RF タグ読み取り時の Inventory 処理中のアンチコリジョン処理において、リーダライタが RF
    タグに対して指定するスロット数を、コリジョンの発生頻度により自動的に増減するための機能
    です。
    「Q 値の自動 UP/DOWN 機能」の詳細は、「3.2.3 Q 値の自動 UP/DOWN 機能」をご参照くだ
    さい。
     ・[使用する]
      RF タグ読み取り時のアンチコリジョン処理において、コリジョンが発生したスロット数に
      応じて、次回のアンチコリジョン処理の際のスロット数（Q 値）を、リーダライタ内部で動
      的に切り替えます。
     ・[使用しない]
      RF タグ読み取り時のアンチコリジョン処理で使用するスロット数（Q 値）は、リーダライ
      タに設定された「Q 値の開始値」に固定されます。
      「Q 値の自動 UP/DOWN 機能」を使用しない場合は、読み取り対象の RF タグの枚数に合
      わせて、「Q 値の開始値」を適切に設定してください。
      「Q 値の開始値」を適切に設定しないと、RF タグを読みこぼしたり、アンチコリジョン処
      理に時間が掛かったりする原因となります。


  ● アンチコリジョン機能 （FLASH 初期値：使用する）
    ・[使用する]
     Inventory 処理においてコリジョンが発生したスロットがあった場合、再度 Inventory 処理を
     おこない、応答を返す RF タグが無くなるまでアンチコリジョン処理を繰り返します。
    ・[使用しない]
     Inventory 処理において、コリジョンが発生したスロットは、RF タグの読み取りをおこないま
     せん。
     コリジョン処理を行わない分、読み取り速度が上がりますが、読み取り枚数にバラツキが発生
     します。
     コリジョンが発生したことを検出しませんので、「Q 値の自動 UP/DOWN 機能」も動作しな
     くなります。Q 値の設定が適切でない場合には、読み取りが不安定になります。


  ● Q 値の開始値 （FLASH 初期値：3）
    ・RF タグ読み取り時の Inventory 処理において、アンチコリジョン処理で使用するスロット数
     （Q 値）の開始値を設定します。
     1 回の Inventory 処理で読み取りをおこなう RF タグの枚数に応じて適切な Q 値の設定として
     ください。
    ※「Q 値の開始値」は、別途指定する「Q 値の最小値」、「Q 値の最大値」との大小関係が、「Q
     値の最小値」≦「Q 値の開始値」≦「Q 値の最大値」となるように指定してください。上記の
     大小関係とならない設定とした場合は、リーダライタから NACK 応答が返ります。
    ※読み取る RF タグ枚数に対してスロット数が小さいと読みこぼす可能性があり、大きすぎると
     処理時間が遅くなります。
    ・Q 値の設定の詳細は、「3.2.2 Q 値設定」をご参照ください。
    ＜注意事項＞Q=11 を超える Q 値の制限
      UTR-S201 では、Q=12 以上に設定した場合、Inventory 処理時間が 4 秒を超える可能性が
      高く、電波法の制限により処理の途中でキャリア OFF となる可能性があるため、
      Q=12 以上を設定した場合であっても、Q=11 の設定で Inventory 処理を実行します。


  ● Inventory の Target （FLASH 初期値：A）
    ・設定可能な値…[A] または [B]
    ・RF タグは Session ごとに Inventoried フラグを持っており、フラグは[A]または[B]の状態を保
     持しています。
     (例) S0=[A], S1=[A], S2=[B], S3=[A]
    ・本設定では、Inventory 処理をおこなう際に、RF タグが持つ Inventoried フラグ（A/B）のう
     ち、どちらのフラグの RF タグを読み取り対象にするかを指定します。
     Session 値と併せて使用します。


  ● Session 値 （FLASH 初期値：S0）
    ・本設定では、Inventory 処理をおこなう際に、RF タグのどの Session の Inventoried フラグを
     参照するかを設定します。
     基本的には、[UHF_SetSelectParam]コマンドで指定した Target と同じ Session を設定しま
     す。
  (例) Session=[S0]、Sel=[ALL]、Inventory の Target = [A]の場合
    → S0=[A]の RF タグのみ読み取りします。他の Session の状態には依存しません。
      ・RF タグ 1 … S0= [A], S1= [A], S2= [B], S3= [A] → 読み取りする
      ・RF タグ 2 … S0= [B], S1= [B], S2= [B], S3= [A] → 読み取りしない
      ・RF タグ 3 … S0= [A], S1= [A], S2= [A], S3= [A] → 読み取りする


  ● Sel 値 （FLASH 初期値：11: SL）
    ・読み取り対象の RF タグの指定に、「Inventoried フラグ」と「SL フラグ」のどちらを使用す
     るかを設定します。
     基本的には、[UHF_SetSelectParam]コマンドで指定した「Target 値」が[SL]の場合は、
     「Sel 値」には[SL]または[^SL]を指定します。
     それ以外の場合は[ALL]を指定します。

    ・Sel 値が[ALL]の場合 (00:ALL または 01:ALL)
                                           「Inventory の Target」で指定
       「Session」値で指定した「Inventoried フラグ」の状態が、
       したフラグになっている RF タグが読み取り対象となります。
       (例) Session=[S0], Sel=[ALL], Inventory の Target= [A]の場合
           →S0=[A]の RF タグのみ読み取りします。他の Session フラグの状態には依存しませ
             ん。
        ・RF タグ 1 … S0= [A], S1= [A], S2= [B], S3= [A], SL=[Set] → 読み取りする
        ・RF タグ 2 … S0= [B], S1= [B], S2= [B], S3= [A], SL=[Set] → 読み取りしない
        ・RF タグ 3 … S0= [A], S1= [A], S2= [A], S3= [A], SL=[Reset] → 読み取りする


       ＜Sel 値が「ALL」の場合の注意点＞
        通常は、[UHF_SetSelectParam]コマンドで指定する「Target 値」と、
        [UHF_SetInventoryParam]コマンドで指定する「Session 値」は、同一の Session とな
        るようにします。
        ※Select コマンドで遷移させた Inventory フラグ以外のフラグを参照して読み取りをお
          こなった場合、Select コマンドは意味を持たなくなります。


    ・Sel 値が「10: ^SL」の場合
       SL フラグが[Reset]で、かつ、     「Session」値で指定した Session の Inventoried フラグの状
       態が、 「Inventory の Target」と一致する RF タグが読み取り対象となります。
       (例) Session=[S0], Sel=[^SL], Inventory の Target= [A]の場合
           →S0=[A]で、かつ、SL=[Reset]の RF タグのみ読み取りします。
             他の Session フラグの状態には依存しません。
        ・RF タグ 1 … S0= [A], S1= [A], S2= [B], S3= [A], SL=[Set] → 読み取りしない
        ・RF タグ 2 … S0= [B], S1= [B], S2= [B], S3= [A], SL=[Set] → 読み取りしない
        ・RF タグ 3 … S0= [A], S1= [A], S2= [A], S3= [A], SL=[Reset] → 読み取りする

    ・Sel 値が「11: SL」の場合
       SL フラグが[Set]で、かつ、      「Session」値で指定した Session の Inventoried フラグの状態
       が、 「Inventory の Target」と一致する RF タグが読み取り対象となります。
       (例) Session=[S0], Sel=[SL], Inventory の Target= [A]の場合
           →S0=[A]で、かつ、SL=[Set]の RF タグのみ読み取りします。
             他の Session フラグの状態には依存しません。
        ・RF タグ 1 … S0= [A], S1= [A], S2= [B], S3= [A], SL=[Set] → 読み取りする
        ・RF タグ 2 … S0= [B], S1= [B], S2= [B], S3= [A], SL=[Set] → 読み取りしない
        ・RF タグ 3 … S0= [A], S1= [A], S2= [A], S3= [A], SL=[Reset] → 読み取りしない


  ● TRext 値 （FLASH 初期値：Use pilot tone）
    ・RF タグからの応答のプリアンブル（同期信号）に「pilot tone」を含むかどうかの設定です。
    ・UTR-S201 シリーズは、[Use pilot tone]のみ対応しています。[No pilot tone]を指定しても反
     映されません。


  ● M 値 (変調度、変調モード)         （FLASH 初期値：M4）
    ・RF タグからの応答信号の符号化方式を指定します。
     M の後の数値が大きい程、応答信号の受信の精度が高くなりますが、応答信号の受信に掛か
     る時間が長くなります。
     特に、大きいデータ長の RF タグデータの読み取りをおこなう場合の、読み取りの精度および
     受信に掛かる時間に影響します。
    ・UTR-S201 シリーズは、[M4]のみ対応しています。[M4]以外の値を指定しても反映されませ
     ん。


  ● DR 値 （FLASH 初期値：64/3）
    ・DR(Divide Ratio)の略で、RF タグからリーダライタへ応答を返す際のデータ転送速度に影響
     します。「DR 値」=[8]よりも「DR 値」=[64/3]のほうが、高速にデータ転送が可能です。
    ・UTR-S201 は、「DR 値」=[8]に未対応です。「DR 値」=[8]を指定しても、設定は変更されま
     せん。


  ● Q 値の最小値 （FLASH 初期値：1）
    ・「Q 値の自動 UP/DOWN 機能」が[使用する]の場合の、Q 値の下限値を指定します。
    ※「Q 値の最小値」は、別途指定する「Q 値の開始値」、「Q 値の最大値」との大小関係が、「Q
     値の最小値」≦「Q 値の開始値」≦「Q 値の最大値」となるように指定してください。上記の
     大小関係とならない設定とした場合は、リーダライタから NACK 応答が返ります。


  ● Q 値の最大値 （FLASH 初期値：8）
    ・「Q 値の自動 UP/DOWN 機能」が[使用する]の場合の、Q 値の上限値を指定します。
    ※「Q 値の最大値」は、別途指定する「Q 値の開始値」、「Q 値の最小値」との大小関係が、「Q
     値の最小値」≦「Q 値の開始値」≦「Q 値の最大値」となるように指定してください。上記の
     大小関係とならない設定とした場合は、リーダライタから NACK 応答が返ります。


  ● MemBank （FLASH 初期値：TID）
    リーダライタの動作モードが「UHF 連続インベントリリードモード」の場合に、EPC 以外に読
    み取りする MemBank を指定します。
    MemBank の詳細は、「4.2 RF タグのメモリ構造」をご参照ください。


  ● TID 付加 （FLASH 初期値：付加しない）
      リーダライタが「UHF 連続インベントリリードモード」で動作する場合に、RF タグの EPC
      および指定 MemBank データの読み取り結果に加えて、TID データも読み取りして付加する
      かどうかを指定します。
      ・[付加する]
        リーダライタは、TID データも読み取りをおこないます。
        上位機器へのレスポンスは、EPC、指定 MemBank データ、TID が返ります。
        TID の読み取りに失敗した場合には、上位機器へのレスポンスは返りません。
     ・[付加しない]
      リーダライタは、TID データの読み取りをおこないません。
      上位機器へのレスポンスは、EPC および指定 MemBank データのみ返ります。

     TID の読み取りフローの詳細は、
                     「3.9 TID 付加読み取り」をご参照ください。


  ● 読み取り開始 Word アドレス （FLASH 初期値：[00 00 00 00]h）
    リーダライタが「UHF 連続インベントリリードモード」動作する場合に、指定 MemBank の読
    み取り開始位置（Word アドレス）を指定します。
     (例) Word アドレス[03]h を指定する場合は、[00 00 00 03]h を指定します。
     (例) Word アドレス[10D]h を指定する場合は、[00 00 01 0D]h を指定します。


  ● 読み取り Word 数 （FLASH 初期値：2）
    リーダライタが「UHF 連続インベントリリードモード」動作する場合に、指定 MemBank の読
    み取るメモリサイズを Word 長（2 バイト単位）で指定します。
    1～32 [Word]の範囲で指定が可能です。


 ［ACK レスポンス］
ラベル名 バイト数                                          内容
 STX         1      02h
アドレス         1      00h（「5.2 通信フォーマットの詳細」参照）
コマンド         1      30h（ACK）
データ長         1      01h
データ部         1      31h（詳細コマンド）
 ETX         1      03h
 SUM         1      SUM 値（「5.3 SUM の計算方法」参照）
  CR         1      0Dh

  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。

  ［コマンド／レスポンス例］
   (例) 以下のパラメータを書き込む場合
                       データ種類                    数値／パラメータ               コマンド列
              書き込み対象                       FLASH データ                [02]h
              Select コマンドの使用               使用する           [1]b
              Q 値の自動 UP/DOWN 機能            使用する           [1]b
                                                                    [0001 1111]b=
パラメータ 1       アンチコリジョン機能                   使用する           [1]b
                                                                    [1F]h
              Q 値の初期値                      3              [0011]b
              Inventory の Target           A              [0]b
              Session 値                    S0             [00]b
              Sel 値                        SL             [11]b
                                                                    [1101 1100]b=
パラメータ 2       TRext 値                      Use pilot tone [1]b
                                                                    [DC]h
              M値                           M4             [10]b
              DR 値                         64/3           [1]b
              Q 値の最小値                      1              [0001]b
パラメータ 3                                                             [81]h
              Q 値の最大値                      8              [1000]b
              MemBank                      TID            [10]b     [0000 0010]b=
パラメータ 4
              TID 付加                       付加しない          [0]b      [02]h
              読み取り開始 Word アドレス             0                        [00 00 00 00]h
              読み取り Word 数                  2                        [02]h

    • コマンド
       02 00 55 0B 31 02 1F DC 81 02 00 00 00 00 02 03 18 0D
    • レスポンス
       02 00 30 01 31 03 67 0D
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

### 8.1 ACK/レスポンス例（設定変更成功時）

| 項目 | 内容 |
|---|---|
| ACK構造 | `02 ADR 30 01 31 03 SUM 0D` |
| `CMD` | `30h`（ACK） |
| `LEN` | `01h` |
| `DATA[0]` | `31h`（詳細コマンド: UHF_SetInventoryParam） |
| PDF掲載レスポンス例 | `02 00 30 01 31 03 67 0D` |
| 注意 | 成功ACKには書き込んだInventory条件値は返りません。反映確認は `55h 41h`（UHF_GetInventoryParam）で読戻してください。 |

設定変更後は、対応する読み取りコマンドで読戻し確認し、RAM変更の場合は終了時に開始値へ復元してください。FLASH変更の場合は再起動後の保持も確認対象です。

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A 31 44 00 00 00 00 00 00 00 00 03 B5 0D` |
| エラーコード1 | `44h: FORMAT_ERROR` |
| 見る場所 | コマンドは`31h`、データ部1byte目はエラー発生元の詳細コマンド、データ部2byte目以降がエラーコードです。 |

NACK時は、エラーコード1だけでなく、UHF ICエラー時のエラーコード2、UHF_Encode/BlockWrite2固有の追加コードも確認してください。予約領域は意味定義がない限り無視します。

### 8.3 設定依存の注意

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
| `CMD=30h` かつ `DATA[0]` が `31h` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h 31h` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` だが書込値の反映を確認していない | `ACK_PENDING_VERIFY` | 必要に応じて対応する読出コマンドで読戻し確認する |

対象識別子: コマンド `55h` / 詳細 `31h` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` は `LEN=01h` の固定長ACKです。書き込んだInventory条件値はACKには含まれません。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `detail` | `31h`: UHF_SetInventoryParam成功ACK |

`LEN` が `01h` 以外、または `DATA[0]` が `31h` 以外の場合は、このコマンドの通常成功ACKとして扱わず、別レスポンスまたは異常フレームとして分類してください。

設定書き込み系は、ACK受信後に必要なら対応する読出コマンドで読戻しし、RAM/FLASHの反映範囲と復元要否を別管理してください。

アンテナ切替完了ACKとキャリア検知ACKを受ける可能性がある受信ループでは、`DATA[0]` と `DATA[1]` の組み合わせで通常ACKと区別してください。


#### NACK分類

このコマンドのNACKは共通NACKとして扱います。`CMD=31h` の場合は、成功ACKではなく、以下のoffsetでエラーとして分類してください。

| DATA offset | フィールド | 解釈 |
|---:|---|---|
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h 31h` |
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

- `../../COMMAND_MASTER_V117.md`
- `../../TRACEABILITY_INDEX_V117.md`
- `../../RESPONSE_AND_NACK_MASTER.md`
- `../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
