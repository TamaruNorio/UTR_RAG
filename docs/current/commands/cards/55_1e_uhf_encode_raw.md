---
title: "UHF_Encode PDF原文転記"
doc_type: "raw_reference"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
verification_status: "DOCUMENTATION_CURRENT"
result_status: "N/A"
related_docs:
  - "55_1e_uhf_encode.md"
tags:
  - "utr-s201"
  - "raw-reference"
---

```text
7.5.10 UHF_Encode
 1回のコマンド送信で、RFタグの複数のMemBankに対してデータを書き込むコマンドです。同時に
 RFタグのメモリをロックすることもできます。
 ※「タカヤ独自コマンド」です。
   [UHF_BlockWrite]、[UHF_Lock]、[Accessパスワードの書き込み]の複合コマンドです。
   RF送信信号(キャリア)の状態により、内部処理で[RF送信信号の制御]コマンドが実行される場合
   があります。コマンド実行後は、実行前のRF送信信号(キャリア)の状態に戻ります。
   従来は複数のコマンド＆レスポンスを送受信する必要があったコマンド群を1つのコマンドとする
   ことで、上位機器とのデータ通信時間を節約し、高速な書き込みが可能となります。

  ［コマンド］
  ラベル名   バイト数                            内容
   STX     1          02h
  アドレス     1          00h（ 「5.2 通信フォーマットの詳細」参照）
  コマンド     1          55h
  データ長     1          下記 (※1) を参照
                1     1Eh（詳細コマンド）
                              BlockWrite コマンドを使用
                      bit0      0：使用しない（Write コマンドを複数回実行します）
                                1：使用する（BlockWrite コマンドを複数回実行します）
                              コマンド実行前のパスワード保持
                      bit1      0: 保持しない
                                1: 保持する
                               Lock 済 RF タグの再書き込み
                                 Reserved 領域書き込み時の Access コマンドの発行
  データ部
                1     bit2         0: 発行しない
                                   1: 発行する
                                 EPC(UII)領域書き込み時の Access コマンドの発行
                      bit3         0: 発行しない
                                   1: 発行する
                                 User 領域書き込み時の Access コマンドの発行
                      bit4         0: 発行しない
                                   1: 発行する
                      bit5-7 将来拡張のための予約（通常は 0）
   （次ページへ続く）


  （前ページからの続き）

 ラベル名       バイト数                        内容
          MemBank 00:Reserved への書き込み内容
                      Reserved 領域への書き込み内容のデータ長
                      ・Reserved 領域への書き込み Word 数×2＋2 を入力します
              1
                           ※Reserved 領域への書き込み Word 数をここで指定します。
                      ・Reserved 領域への書き込みを行わない場合には 0 を指定します
            ※Reserved 領域への書き込みをおこなう場合、以下を指定します。
                      書き込み開始 Word アドレス
                      ：メモリ上の書き込み開始位置（Word 単位）
              2
                         1 バイト目：上位バイト(MSB)
                         2 バイト目：下位バイト(LSB)
            書き込み
                      書き込みデータ（最大 123[Word] ※2）
           Word 数×2
          MemBank 01:EPC(UII)への書き込み内容
                      EPC(UII)領域への書き込み内容のデータ長
                      ・EPC(UII)領域への書き込み Word 数×2＋2 を入力します
              1
                           ※EPC(UII)領域への書き込み Word 数をここで指定します。
                      ・EPC(UII)領域への書き込みを行わない場合には 0 を指定します
            ※EPC(UII)領域への書き込みをおこなう場合、以下を指定します。
 データ部
                      書き込み開始 Word アドレス
                      ：メモリ上の書き込み開始位置（Word 単位）
              2
                         1 バイト目：上位バイト(MSB)
                         2 バイト目：下位バイト(LSB)
            書き込み
                      書き込みデータ（最大 123[Word] ※2）
           Word 数×2
          MemBank 11:User への書き込み内容
                      User 領域への書き込み内容のデータ長
                      ・User 領域への書き込み Word 数×2＋2 を入力します
              1
                           ※User 領域への書き込み Word 数をここで指定します。
                      ・User 領域への書き込みを行わない場合には 0 を指定します
            ※User 領域への書き込みをおこなう場合、以下を指定します。
                      書き込み開始 Word アドレス
                      ：メモリ上の書き込み開始位置（Word 単位）
              2
                         1 バイト目：上位バイト(MSB)
                         2 バイト目：下位バイト(LSB)
            書き込み
                      書き込みデータ（最大 123[Word] ※2）
           Word 数×2
  （次ページへ続く）


  （前ページからの続き）

 ラベル名      バイト数                              内容
          Lock 情報
                    Lock コマンドの使用（Lock 情報のデータ長）
               1      00h：使用しない
                      03h：使用する
             ※Lock コマンドを使用する場合、以下のパラメータ 1～3 を指定します。
                    パラメータ 1
                     ビット            処理対象             処理種別         フラグ
                    bit0    TID 領域             PermaLock          Mask
                    bit1    TID 領域             PasswordWrite      Mask
             (1)    bit2    EPC 領域             PermaLock          Mask
              ※3    bit3    EPC 領域             PasswordWrite      Mask
                    bit4    Access Password 領域 PermaLock          Mask
                    bit5    Access Password 領域 PasswordRead/Write Mask
                    bit6    Kill Password 領域   PermaLock          Mask
                    bit7    Kill Password 領域   PasswordRead/Write Mask
                    パラメータ 2
                     ビット            処理対象             処理種別         フラグ
 データ部               bit0    EPC 領域             PermaLock          Action
                    bit1    EPC 領域             PasswordWrite      Action
             (1)    bit2    Access Password 領域 PermaLock          Action
              ※3    bit3    Access Password 領域 PasswordRead/Write Action
                    bit4    Kill Password 領域   PermaLock          Action
                    bit5    Kill Password 領域   PasswordRead/Write Action
                    bit6    User 領域            PermaLock          Mask
                    bit7    User 領域            PasswordWrite      Mask
                    パラメータ 3
                    ビット             処理対象             処理種別         フラグ
                    bit0    0 固定
                    bit1    0 固定
             (1)    bit2    0 固定
              ※3    bit3    0 固定
                    bit4    User 領域            PermaLock          Action
                    bit5    User 領域            PasswordWrite      Action
                    bit6    TID 領域             PermaLock          Action
                    bit7    TID 領域             PasswordWrite      Action
  ETX        1      03h
  SUM        1      SUM 値（ 「5.3 SUM の計算方法」参照）
   CR        1      0Dh


※1：データ長は、それぞれのMemBankへの書き込みの有無や、Lockコマンドの発行の有無に
   応じて、以下の計算式で求めます。
    (1) 初期値を[06]hとします。
    (2) [Reserved 領域への書き込み内容のデータ長]で指定したデータ長を加算します。
    (3) [EPC(UII)領域への書き込み内容のデータ長]で指定したデータ長を加算します。
    (4) [User領域への書き込み内容のデータ長]で指定したデータ長を加算します。
    (5) [Lock情報のデータ長]で指定したデータ長を加算します。
    ※ データ長が255[byte] (=[FF]h)を超える指定はできません。
     (例) Kill Password 2[Word]、Access Password 2[Word]、Stored PC 1[Word]およびEPC 6[Word]
         (=96[bit])の書き込みをおこない、Lockコマンドを使用する場合、
         User領域へは、最大で109[Word]までの書き込みが可能です。
            (1) 初期値 = 6
            (2) [Reserved領域への書き込み内容のデータ長] = (2+2)×2+2 = 10
            (3) [EPC(UII)領域への書き込み内容のデータ長] = (1+6)×2+2 = 16
            (4) [User領域への書き込み内容のデータ長] = 109×2+2 = 220
            (5) [Lock情報のデータ長]=3
            → データ長 = 6+10+16+220+3 = 255 (=[FF]h)

※2：各MemBankへの書き込み内容およびLock情報を含めたデータ長を255[byte] (=[FF]h)以下とす
   る必要があります。そのため、書き込みするMemBankが複数にわたる場合や、Lock処理をおこ
   なう場合は、データ長の合計が255[byte]を超えないように注意してください。

※3：パラメータ1～パラメータ3について
 ・「Lockコマンドの使用」で[使用する]を選択した場合、パラメータ1～3にLock処理内容を
  指定します。
 ・「Lockコマンドの使用」で[使用しない]を選択した場合は、パラメータ1～3は省略します


● BlockWriteコマンドを使用
    RF タグへの書き込みに BlockWrite コマンドを使用するかどうかを選択します。
  ・[使用する]
   BlockWrite コマンドを使用して RF タグへの書き込みをおこないます。
     上位機器からリーダライタへは複数 Word の書き込みデータの指定をおこないますが、リー
     ダライタから RF タグへは 1[Word]ごとに分けて複数回書き込みをおこないます。
     そのため、RF タグへの書き込みの途中で失敗して NACK 応答となった場合、書き込み内容
     の途中まで書き込みが成功している場合があります。
       ※BlockWrite コマンドは ISO18000-63 では RF タグのオプションコマンドのため、一部の
        RF タグでは対応していません。詳細は「4.2.7 RF タグオプションコマンド対応表」また
        は使用する RF タグ Chip のデータシートを参照ください。

  ・[使用しない]
   Write コマンドを使用して RF タグへの書き込みをおこないます。
     上位機器からリーダライタへは複数 Word の書き込みデータの指定をおこないますが、リー
     ダライタから RF タグへは 1[Word]ごとに分けて複数回書き込みをおこないます。
     そのため、RF タグへの書き込みの途中で失敗して NACK 応答となった場合、書き込み内容
     の途中まで書き込みが成功している場合があります。


● コマンド実行前のパスワード保持
   本コマンドは、   コマンド実行中に RF タグの Reserved 領域(Access パスワード)を書き換えたり、
   RF タグの Lock の[設定]／[解除]をおこなったりするため、コマンド実行中にリーダライタの
   Access パスワードを書き換えます。
    本設定で、UHF_Encode コマンド実行後に、コマンド実行前にリーダライタに書き込まれていた
    Access パスワードを保持するかどうかを選択します。

＜コマンドの実行に成功した場合 (ACK 応答) ＞
 ● [保持する]を選択した場合
   コマンド実行後、リーダライタの Access パスワードには、コマンド実行前に
   リーダライタに書き込まれていた Access パスワードが書き込まれます。
     ※同一の Access パスワードを持つ、異なる RF タグに続けて書き込んだり、
      Access パスワードが設定されていない RF タグ(Access パスワード=[0000 0000]h)に対して
      連続して書き込んだりする場合に推奨の設定です。
     ※本コマンドで RF タグの Access パスワードを書き換えた場合、書き換え後の RF タグに対
      して続けて RF タグ通信コマンドを実行した場合、リーダライタと RF タグの Access パス
      ワードが「不一致」となりますので、Access パスワードエラーとなります。

  ● [保持しない]を選択した場合
    ・RF タグの Access Password 領域(Reserved 領域の 02h から 2[Word])に書き込みを
     おこなう場合
     →コマンド実行後、リーダライタの Access パスワードには、RF タグの Access Password 領
      域に書き込んだ内容が書き込まれます。
       ※ベリファイのための Read をおこなうなど、同一の RF タグに対して、続けて[RF タグ通
        信コマンド]を実行する場合に推奨の設定です。

    ・RF タグの Access Password 領域(Reserved 領域の[02]h から 2[Word])に書き込みを
     おこなわない場合
     →コマンド実行後、リーダライタの Access パスワードには、[0000 0000]h が書き込まれます。
       ※Access Password が設定されていない RF タグ(Access Password=[0000 0000]h)に対して、
        Access Password 領域以外の領域を連続して書き込む場合に推奨の設定です。


  ＜コマンドの実行に失敗した場合 (NACK 応答) ＞
   ● [保持する]を選択した場合
       コマンド実行後、リーダライタの Access パスワードには、コマンド実行前に
       リーダライタに書き込まれていた Access パスワードを書き込まれます。

    ● [保持しない]を選択した場合
     ・RF タグの Access パスワード領域(Reserved 領域の[02]h から 2[Word])に書き込みを
      おこなう場合
       ・Reserved 領域への書き込みに成功した場合
          →コマンド実行後、リーダライタの Access パスワードには、RF タグの
            Access パスワード領域に書き込んだ内容が書き込まれます。
       ・Reserved 領域への書き込みに失敗した場合、または、Reserved 領域の書き込み前にコマ
        ンドに失敗した場合
          →コマンド実行後、リーダライタの Access パスワードには、コマンド実行前に
            リーダライタに書き込まれていた Access パスワードが書き込まれます。
         ※RF タグの Access パスワード領域への書き込み内容が[0000 0000]h か否かで書き込み
          の順序が変わります。詳細は、＜注意事項＞ コマンド内部の処理手順をご確認くださ
          い。

     ・RF タグの Access パスワード領域(Reserved 領域の[02]h から 2[Word])に書き込みを
      おこなわない場合
         →コマンド実行後、リーダライタの Access パスワードには、コマンド実行前に
          リーダライタに書き込まれていた Access パスワードが書き込まれます。


● Lock 済 RF タグの再書き込み
    UHF_Encode コマンドは複数の MemBank に対して書き込みをおこなうコマンドのため、
    MemBank によっては Password Write Lock（または、Password Read/Write Lock）が掛かって
    いる場合と掛かっていない場合があります。
    Password Write Lock または Password Read/Write Lock が設定されている RF タグに対して書
    き込みをおこなう場合、BlockWrite コマンドや Write コマンドを発行する前に、リーダライタ
    の Access パスワードと RF タグの Access パスワードが一致している状態で Access コマンドを
    発行する必要があります。
    本設定で、それぞれの MemBank の書き込み前に、Access コマンドを「発行する／発行しない」
    を個別に選択できます。
      ・Write Lock されている MemBank への書き込み時には「発行する」を選択します。
      ・Write Lock されていない MemBank への書き込み時には「発行しない」を選択します。

      複数の MemBank に「発行する」を選択した場合においても、RF タグの複数 MemBank に対
      して読み書きする際には、リーダライタと RF タグ間での Access コマンドの発行は、最初の 1
      回のみおこなわれます。
      Access コマンドでの認証に成功した場合、RF タグは Open 状態から Secured 状態に遷移する
      ため、続けて実行する書き込みや Lock 処理などは Access コマンドを発行せずに実行可能なた
      めです。

      以下に、「Lock 済 RF タグの再書き込み」MemBank 指定のフローチャートを示します。


                 RF タグの Access パスワ
                 ードに書き込む内容は？

  [0000 0000]h
     または                   [0000 0000]h 以外
  書き込まない
                                             Yes   Reserved 領域書き込み時の
                 Reserved 領域の書き込み                    Access コマンドの発行
                 かつ Lock されている？                             を指定


                           No

                                             Yes   EPC(UII)領域書き込み時の
                 EPC(UII)領域に書き込み
                                                     Access コマンドの発行
                 かつ Lock されている？
                                                            を指定

                           No

                                             Yes    User 領域書き込み時の
                  User 領域に書き込み
                                                    Access コマンドの発行
                 かつ Lock されている？                            を指定

                           No

                                             Yes   Reserved 領域書き込み時の
                 Reserved 領域に書き込み
                                                     Access コマンドの発行
                 かつ Lock されている？
                                                            を指定

                           No
                  Lock 済 RF タグの
                 再書き込みを指定しない


  ・Reserved領域書き込み時のAccessコマンドの発行
     書き込み対象のRFタグのAccess Passwordまたは、Kill PasswordがRead/Writeロックされて
     いる場合に使用します。
     本パラメータを「発行する」に設定することで、RFタグのReserved領域への書き込みをおこ
     なう際にAccessコマンドを発行します。
       ・Reserved領域への書き込み時のAccessコマンド発行時に使用するAccessパスワードは、
        コマンド実行時にリーダライタに設定されているAccessパスワードです。
        リーダライタには、[Accessパスワードの書き込み]コマンドを使用して、あらかじめ
        Accessパスワードを書き込んでおく必要があります。

  ・EPC(UII)領域書き込み時のAccessコマンドの発行
    書き込み対象のRFタグのEPC(UII)領域がWriteロックされている場合に使用します。
    本パラメータを「発行する」に設定することで、RFタグのEPC(UII)領域への書き込み時に
    Accessコマンドを発行します。
       ・コマンドパラメータでAccess Password (Reserved領域の[02]hと[03]h)の書き込みを
        指定している場合は、そのAccess Passwordを使用します。
       ・コマンドパラメータでAccess Passwordの書き込みを指定していない場合には、
        リーダライタに設定されたAccess Passwordを使用します。
         ※リーダライタにAccess Passwordが設定されていない場合には、Accessコマンドを発
          行できず、NACK応答となります。

  ・User領域書き込み時のAccessコマンドの発行
    書き込み対象のRFタグのUser領域がWriteロックされている場合に使用します。
    本パラメータを「発行する」に設定することで、RFタグのUser領域への書き込み時にAccess
    コマンドを発行します。
       ・コマンドパラメータでAccess Password (Reserved領域の[02]hと[03]h)の書き込みを
        指定している場合は、そのAccess Passwordを使用します。
       ・コマンドパラメータでAccess Passwordの書き込みを指定していない場合には、
        リーダライタに設定されたAccess Passwordを使用します。
         ※リーダライタにAccess Passwordが設定されていない場合には、Accessコマンドを発
          行できず、NACK応答となります。


● 各MemBankへの書き込み内容
   Reserved領域、EPC(UII)領域、User領域に対して、それぞれのMemBankへの書き込みの内容
   を設定します。
  ● 書き込み開始Wordアドレス
     指定した MemBank 上の書き込み開始位置（Word アドレス）を指定します。
  ● 書き込みデータ
     書き込むデータを指定します。


● Lock情報
    各 MemBank に対して Lock の内容を設定します。
    詳細は、「7.5.6 UHF_Lock」をご参照ください。

  ＜注意事項＞ Lock 処理時の Access コマンド発行時の Access Password
     本コマンドでは、Lock コマンドを発行する際に、Access コマンドが発行されます。Access コ
     マンド発行時に使用する Access パスワードの優先順位は、以下の通りです。
      ・コマンドパラメータでAccess Password (Reserved領域の[02]hと[03]h)の書き込みを
       指定している場合は、そのAccess Passwordを使用します。
       ・コマンドパラメータでAccess Passwordの書き込みを指定していない場合には、
        リーダライタに設定されたAccess Passwordを使用します。
         ※リーダライタにAccess Passwordが設定されていない場合には、Accessコマンドを発
          行できず、NACK応答となります。


＜注意事項＞ コマンド内部の処理手順
  本コマンドの内部処理では、RF タグに書き込む Access パスワードに[00000000]h が指定された場
  合と、指定されなかった場合で異なる処理手順としています。
   ※リーダライタの Access パスワードに[00000000]h を指定すると、Access コマンドが発行でき
    なくなるため

    ・Reserved 領域の Access パスワードの書き込み内容に[00000000]h 以外を指定した場合は、
     以下の順番で内部処理をおこないます。
     (1) Reserved 領域への書き込み
     (2) EPC(UII)領域への書き込み
     (3) User 領域への書き込み
     (4) Lock 処理を実行
     (5) コマンドパラメータに応じてリーダライタへの Access パスワードの書き込み

    ・Reserved 領域の Access パスワードの書き込み内容に[00000000]h を指定した場合は、
     以下の順番で内部処理をおこないます。
     (1) EPC(UII)領域への書き込み
     (2) User 領域への書き込み
     (3) Lock 処理を実行
     (4) Reserved 領域の書き込み
     (5) コマンドパラメータに応じてリーダライタへの Access パスワードの書き込み


 ［ACK レスポンス］
ラベル名 バイト数                            内容
 STX        1    02h
アドレス        1    00h（「5.2 通信フォーマットの詳細」参照）
 ACK        1    30h
データ長        1    01h
データ部        1    1Eh（詳細コマンド）
 ETX        1    03h
 SUM        1    SUM 値（「5.3 SUM の計算方法」参照）
  CR        1    0Dh


  ［NACK レスポンス］
  「7.6 NACK レスポンスとエラーコード」参照。

    ＜注意事項＞ 処理失敗時の NACK レスポンス
       本コマンドを実行した結果、NACK 応答が返った場合、指定した領域の途中まで処理が完了し
       ている可能性があります。
       どの処理まで完了したか確認する場合、NACK レスポンス 8[byte]目のエラーコード 3 を参照
       します。詳細は、「7.6 NACK レスポンスとエラーコード」をご参照ください。
       なお、本コマンドで NACK 応答となる場合、  「コマンド実行前のパスワード保持」にて指定し
       たパラメータ、および、Reserved 領域の書き込みに成功したかにより、コマンド実行後にリー
       ダライタに書き戻される Access パスワードが異なります。詳細は、「● コマンド実行前のパス
       ワード保持」をご確認ください。

       ・エラーコード 3 に返るエラーコード
        (1) Reserved 領域への書き込みで NACK 応答となった場合、
            エラーコード 3 に、[01h: Reserved 領域への書き込み時にエラー]が返ります。
        (2) EPC(UII)領域への書き込みで NACK 応答となった場合、
            エラーコード 3 に、[02h: EPC(UII)領域への書き込み時にエラー]が返ります。
        (3) User 領域への書き込みで NACK 応答となった場合、
            エラーコード 3 に、[03h: User 領域への書き込み時にエラー]が返ります。
        (4) Lock 処理の実行で NACK 応答となった場合、
            エラーコード 3 に、[05h: Lock コマンド発行時にエラー]が返ります。


◆ UHF_Encode コマンドを使用することによる処理高速化の概要
 RF タグの複数の MemBank に書き込みをおこなう場合や、Lock 処理を同時におこなう場合に、本
 コマンドを使用して処理内容を一括で送信することにより、上位機器とリーダライタ間の通信回数
 を減らすことができ、従来の手法(複数コマンドを逐次送信する方法)と比較して処理の高速化が可能
 です。


 ● 従来の処理方法 （複数コマンドを逐次送信する方法）
  複数の MemBank への書き込みをおこない、RF タグの Lock をおこなう場合、従来は、上位機器
  から[UHF_BlockWrite]コマンド、[Access パスワードの書き込み]コマンド、[UHF_Lock]コマン
  ドを逐次送信する必要がありました。

         上位機器                              リーダライタ                       RF タグ

 UHF_BlockWrite コマンド    送信
    (※Reserved 領域)           コマンド     受信
                                            内部処理
                                                     送信            BlockWrite コマンド
                                                          コマンド     受信
                                                                         内部処理
                                                                   送信
                                                    受信     レスポンス
                                            内部処理
                                      送信
 受信処理 ※ユーザ側処理          受信     レスポンス
 UHF_BlockWrite コマンド   送信
    (※EPC(UII)領域)            コマンド     受信
                                            内部処理
                                                    送信             BlockWrite コマンド
                                                          コマンド     受信
                                                                         内部処理
                                                                   送信
                                                    受信     レスポンス
                                            内部処理
                                      送信
 受信処理 ※ユーザ側処理          受信     レスポンス
 UHF_BlockWrite コマンド   送信
     (※User 領域)              コマンド     受信
                                            内部処理
                                                    送信             BlockWrite コマンド
                                                          コマンド     受信
                                                                         内部処理
                                                                   送信
                                                    受信     レスポンス
                                            内部処理
                                      送信
 受信処理 ※ユーザ側処理          受信     レスポンス
 Access パスワードの書き込み     送信
                             コマンド     受信
                                            内部処理
                                      送信
 受信処理 ※ユーザ側処理          受信     レスポンス         Access パスワードの書き込み
 UHF_Lock コマンド         送信
                             コマンド     受信
                                            内部処理
                                                    送信             Lock コマンド
                                                          コマンド     受信
                                                                         内部処理
                                                                   送信
                                                    受信     レスポンス
                                            内部処理
                                      送信
 受信処理 ※ユーザ側処理          受信     レスポンス
 Access パスワードの書き込み     送信
                             コマンド     受信
                                            内部処理
                                      送信
 受信処理 ※ユーザ側処理          受信     レスポンス         Access パスワードの書き込み
                   完了


● UHF_Encode コマンドを使用した処理方法 （複数コマンドの一括送信）
  本コマンドを使用することで、上位機器から複数の MemBank への書き込み内容や、Lock の処理
  内容を一括で送信することができます。また、リーダライタ側で一連の処理内容を記憶し、RF タ
  グへのコマンド送信を順次実行することにより、上位機器とリーダライタ間の通信回数を削減
  し、一連の処理の高速化を実現します。

       上位機器                          リーダライタ                       RF タグ

    UHF_Encode    送信
     コマンド                       受信
                       コマンド           内部処理
                                              送信             BlockWrite (Reserved)
                                                    コマンド     受信
                                                                    内部処理
                                                             送信
                                              受信     レスポンス
                                      内部処理
                                              送信          BlockWrite (EPC(UII))
                                                    コマンド     受信
                                                                    内部処理
                                                             送信
                                              受信     レスポンス
                                      内部処理
                                              送信          BlockWrite (User)

                                                    コマンド     受信
                                                                    内部処理
                                                             送信
                                     内部処理     受信     レスポンス
  ※1: RF タグに書き込んだものと
                           Access パスワードの書き込み (※1)
      同じ Access パスワードを
      リーダライタに書き込みます。                 内部処理     送信             Lock コマンド

                                                    コマンド     受信
                                                                    内部処理
                                                             送信
                                  内部処理        受信     レスポンス
                           Access パスワードの書き込み (※2)
                                                    ※2: コマンドのパラメータ設定により、
                           送信     内部処理
                                                        リーダライタに書き込む
   受信処理           受信   レスポンス                            Access パスワードが異なります。
   ※ユーザ側処理

                 完了


  ＜注意事項＞ [UHF_Encode]コマンドを[RF 送信信号の制御]コマンドと組み合わせて使用
         した場合の、コマンド実行後のキャリア出力状態とハンドル維持について
  ・「キャリア ON の維持状態」で本コマンドを実行した場合のリーダライタ内部処理
    リーダライタが RF タグのハンドルを維持している場合は、同じハンドルで書き込み処理をお
    こないます。
    リーダライタが RF タグのハンドルを維持していない場合は、内部の最初のコマンド実行前に
    Q=0 で Inventory 処理を実行して RF タグのハンドルを取得します。
    また、本コマンド終了後に、リーダライタは「キャリア ON の維持状態」を継続します。

  ・「キャリア OFF の状態」で本コマンドを実行した場合のリーダライタ内部処理
    リーダライタの内部処理で、一連の書き込み開始の前に[RF 送信信号の制御]コマンドを発行
    して「キャリア ON の維持状態」にします。
    内部の最初のコマンド実行前に Q=0 で Inventory 処理を実行して、RF タグのハンドルを取
    得します。一連の書き込み実行中は RF タグのハンドルを維持します。
    また、本コマンド終了時に、リーダライタは「キャリア OFF の状態」に戻り、RF タグのハ
    ンドルを破棄します。


＜UHF_Encode コマンドによる処理時間短縮の例＞
・BlockWrite コマンドを使用して EPC 領域:4[Word]、User 領域:2[Word]、Reserved 領域:4[Word]
 の書き込みをおこない、Lock コマンドで特定の MemBank のロックをおこなう場合
・書き込み対象は、Impinj 社製 Monza4QT の Chip を内蔵している RF タグとします。
・書き込み内容は、後述の［コマンド／レスポンス例］の(例 1)に示す内容と同じとします。
     ※本実行時間は、一例です。RF タグの Chip により RF タグ通信コマンドの応答が異なった
      り、同じ Chip の RF タグでもばらついたりする場合があります。
      また、書き込みエラーによる内部リトライ処理による遅延の可能性があります。
      運用前には、実際に使用する RF タグでお試しください。

● UHF_Encode コマンドを使用する場合
              コマンド名                            実行内容                       実行時間
                                     キャリア ON/OFF 制御
                                     複数の MemBank の書き込み
     UHF_Encode                                                              115 msec
                                     各 MemBank の Lock
                                     Access パスワードの内部制御
  送信コマンド(例)
   /* UHF_Encode */
      02 00 55 23 1E 01 0A 00 00 <PASSWORD_BYTES> <PASSWORD_BYTES> 0A 00 02 11 11 22 22 33 33 44 44 06 00
      00 55 55 66 66 03 28 0A 00 03 1B 0D

● UHF_Encode コマンドを使用しない場合
             コマンド名                               実行内容                     実行時間
     RF 送信信号の制御                      キャリア ON                                48 msec
     UHF_BlockWrite                  EPC 領域 4[Word]の書き込み                    49 msec
     UHF_BlockWrite                  User 領域 2[Word]の書き込み                   22 msec
     UHF_BlockWrite                  Reserved 領域 4[Word]の書き込み               39 msec
     Access パスワードの書き込み               Password:<PASSWORD_VALUE>                      22 msec
     UHF_Lock                        各 MemBank の WriteLock                  38 msec
     Access パスワードの書き込み               Password:00000000                      21 msec
     RF 送信信号の制御                      キャリア OFF                               22 msec
              合 計                                                          261 msec

  送信コマンド(例)
   /* RF 送信信号の制御 */
      02 00 4E 02 9E 01 03 F4 0D
   /* UHF_BlockWrite */
      02 00 55 11 1A 01 01 00 00 00 02 00 04 11 11 22 22 33 33 44 44 03 E1 0D
   /* UHF_BlockWrite */
      02 00 55 0D 1A 01 03 00 00 00 00 00 02 55 55 66 66 03 FD 0D
   /* UHF_BlockWrite */
      02 00 55 11 1A 01 00 00 00 00 00 00 04 <PASSWORD_BYTES> <PASSWORD_BYTES> 03 EE 0D
   /* Access パスワードの書き込み */
      02 00 55 07 33 03 00 <PASSWORD_BYTES> 03 AB 0D
   /* UHF_Lock */
      02 00 55 04 18 28 0A 00 03 A8 0D
   /* Access パスワードの書き込み */
      02 00 55 07 33 03 00 00 00 00 00 03 97 0D
   /* RF 送信信号の制御 */
      02 00 4E 02 9E 00 03 F3 0D


  ［コマンド／レスポンス例］
    (例 1) UHF_Encode コマンドを使用して以下のパラメータを書き込む場合
     ※ RF タグの複数 MemBank に内容を書き込み、Lock 処理する手順を想定
      ・本コマンド実行前に、リーダライタの Access パスワードには[0000 0000]h が書き込まれ
        ていて、RF タグの各 MemBank はロック設定されていないと仮定します。
        データ種類                      数値／パラメータ                          コマンド列
        BlockWrite コマンドを使用         bit0… 1: 使用する
        コマンド実行前のパスワード保持            bit1… 0: 保持しない
        Lock 済 RF タグの再書き込み ※Access コマンドの発行                           (00000001)b
        Reserved 領域書き込み時           bit2… 0: 発行しない                     = 01h
        EPC(UII) 領域書き込み時           bit3… 0: 発行しない
        User 領域書き込み時               bit4… 0: 発行しない
        MemBank 00:Reserved
          データ長(書き込み Word 数= 4)     4×2+2 = 10 = 0Ah                  0A
          書き込み開始 Word アドレス         0                                 00 00
          書き込みデータ(Kill Password)   <PASSWORD_BYTES>                       ←
          書き込みデータ(Access Password) <PASSWORD_BYTES>                       ←
        MemBank 01:EPC(UII)
          データ長(書き込み Word 数= 4)     4×2+2 = 10 = 0Ah                  0A
          書き込み開始 Word アドレス         2                                 00 02
          書き込みデータ                  11 11 22 22 33 33 44 44
        MemBank 11:USER
          データ長(書き込み Word 数= 2)     2×2+2 = 6 = 06h                   06
          書き込み開始 Word アドレス         0                                 00 00
          書き込みデータ                  55 55 66 66
        Lock 情報
          Lock コマンドの使用             03h: 使用する                         03
          Lock の処理内容               ※以下を参照                            28 0A 00
       ※データ長は、6 + 10 + 10 + 6 + 3 = 35 = [23]h となります。

     ※Lock 情報：EPC Memory、Access Password の Password ロック設定
     データ種類      処理対象／処理種別                処理種別          フラグ                   コマンド列
     パラメータ    bit3: EPC Memory      PasswordWrite      Mask                  (00101000)b
       1      bit5: Access Password PasswordRead/Write Mask                     = 28h
     パラメータ    bit1: EPC Memory      PasswordWrite      Action                (00001010)b
       2      bit3: Access Password PasswordRead/Write Action                   = 0Ah
     パラメータ                                                                   (00000000)b
                         指定なし                     ―――                ―
       3                                                                        = 00h

    • コマンド
       02 00 55 23 1E 01 0A 00 00 <PASSWORD_BYTES> <PASSWORD_BYTES> 0A 00 02 11 11 22 22 33 33 44 44 06
       00 00 55 55 66 66 03 28 0A 00 03 1B 0D

    • レスポンス
       02 00 30 01 1E 03 54 0D

    ・書き込み後は、リーダライタの Access パスワードは[<PASSWORD_WORDS>]h となります。


    (例 2) UHF_Encode コマンドを使用して以下のパラメータを書き込む場合
     ※ RF タグを再使用する際の初期化を想定
      ・例 1 で作成した RF タグの Lock を解除し、全 MemBank の内容を 0 に戻す際の書き込
        みを想定しています。リーダライタの Access パスワードには[<PASSWORD_VALUE>]h が書き込まれ
        ていると仮定します。
       データ種類                         数値／パラメータ                コマンド列
       BlockWrite コマンドを使用            bit0… 1: 使用する
       コマンド実行前のパスワード保持               bit1… 0: 保持しない
       Lock 済 RF タグの再書き込み ※Access コマンドの発行                    (00001001)b
       Reserved 領域書き込み時              bit2… 0: 発行しない          = 09h
       EPC(UII) 領域書き込み時              bit3… 1: 発行する
       User 領域書き込み時                  bit4… 0: 発行しない
       MemBank 00:Reserved
         データ長(書き込み Word 数= 4)        4×2+2 = 10 = 0Ah        0A
         書き込み開始 Word アドレス            0                       00 00
         書き込みデータ(Kill Password)      00 00 00 00             ←
         書き込みデータ(Access Password) 00 00 00 00                ←
       MemBank 01:EPC(UII)
         データ長(書き込み Word 数= 4)        4×2+2 = 10 = 0Ah        0A
         書き込み開始 Word アドレス            2                       00 02
         書き込みデータ                     00 00 00 00 00 00 00 00
       MemBank 11:USER
         データ長(書き込み Word 数= 2)        2×2+2 = 6 = 06h         06
         書き込み開始 Word アドレス            0                       00 00
         書き込みデータ                     00 00 00 00
       Lock 情報
         Lock コマンドの使用                03h: 使用する               03
         Lock の処理内容                  ※以下を参照                  88 00 00
      ※データ長は、6 + 10 + 10 + 6 + 3 = 35 = 23h となります。

    ※Lock 情報：EPC Memory、Access Password の Password ロック解除
  データ種類      処理対象／処理種別                処理種別          フラグ     コマンド列
           bit3: EPC Memory      PasswordWrite      Mask
  パラメータ 1                                                (00101000)b= 28h
           bit5: Access Password PasswordRead/Write Mask
  パラメータ 2          指定なし                 ―――          ―   (00000000)b= 00h
  パラメータ 3          指定なし                 ―――          ―   (00000000)b= 00h

  RF タグに書き込む Access パスワードに[0000 0000]h を指定しているので、内部のコマンド処理
  は、EPC 領域→User 領域→Lock 処理→Reserved 領域の順になります。
  （※＜注意事項＞ コマンド内部の処理手順を参照）
  EPC 領域が PasswordWrite ロック設定された RF タグに対して書き込みをおこなうので、 「Lock
  済 RF タグの再書き込み」で「EPC(UII)領域書き込み時：発行する」を指定します。
    • コマンド
       02 00 55 23 1E 09 0A 00 00 00 00 00 00 00 00 00 00 0A 00 02 00 00 00 00 00 00 00 00 06
       00 00 00 00 00 00 03 28 00 00 03 EB 0D
    • レスポンス
       02 00 30 01 1E 03 54 0D
    ・書き込み後は、リーダライタの Access パスワードは[<PASSWORD_WORDS>]h となります。
```
