---
title: "UHF_ThroughCmd"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.11"
command_group: "rf_tag_communication"
command_name: "UHF_ThroughCmd"
command_byte: "55h"
detail_command: "FFh"
subcommand: null
operation_profile: "tag-memory-or-high-impact"
operation_level: "RF diagnostic"
rf_emission: true
write_operation: false
flash_operation: false
tag_memory_operation: true
requires_rom_check: true
requires_antenna: true
requires_tag: true
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
  - "rf-tag-communication"
  - "rf-emission"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "pass-with-notes"
---

# UHF_ThroughCmd（高度なタグ直接コマンド）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_ThroughCmd** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.11`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: RF diagnostic
- コマンドバイト: `55h` / 詳細コマンド: `FFh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**UHF_ThroughCmd** です。

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
| タグメモリ操作 | あり |
| ROM確認 | あり |
| アンテナ条件確認 | あり |
| タグ条件確認 | あり |
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

以下は、公式PDF `7.5.11` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.5.11 UHF_ThroughCmd
   RFタグと直接交信するためのコマンドです。
   リーダライタは、上位機器から受信したコマンドをそのままRFタグへ送信し、RFタグからのレス
   ポンスをそのまま上位機器へ送信します。
   ＜注意事項＞
   ・RFタグへ送信するコマンドデータ、RFタグから受信するレスポンスデータのフォーマットは、
    RFタグのデータシートまたはISO/IEC18000-63の規格書を参照してください。
    実行するコマンド仕様にしたがい、上位側でコマンドデータ列の生成、受信データ解析をおこ
    なう必要があります。
   ・本コマンドは、RFタグの状態がOpen状態、もしくはSecured状態の場合に使用可能です。
    そのため、本コマンドを実行する場合は以下の手順が必要となります。
    1．[RF送信信号の制御]コマンドを実行し、キャリア出力をONする。（必須処理）
    2．[UHF_Inventory]コマンドを以下のパラメータで実行し、RFタグをOpen状態とする。
     （必須処理）
     ・Q値の自動UP/DOWN機能=使用しない
     ・Q値の開始値=0
     ・Q値の最小値=0
     ・Q値の最大値=0
       ※複数のRFタグから1枚を指定して処理をおこなう場合は、事前にSelectコマンドを実行す
         る設定も必要です。
    3．[UHF_GetHandle]コマンドを実行してHandleデータを取得する。
                                            （必要に応じて）
       ※Handleを自動で付加する設定の場合は不要な処理です。
    4．[UHF_ThroughCmd]を使用してRFタグのカスタムコマンドを実行する。
    5．[RF送信信号の制御]コマンドを実行し、キャリア出力をOFFする。      （推奨処理）
       ※不要な電波を出し続けると電波干渉の要因となりますので、処理終了後は直ちにキャリ
         ア出力OFFすることを推奨します。


  [コマンド]
    ラベル名     バイト数                       内容
     STX       1      02h
    アドレス       1      00h（ 「5.2 通信フォーマットの詳細」参照）
    コマンド       1      55h
    データ長       1      データ部のデータ長
               1      FFh（詳細コマンド）
                      動作パラメータ
                              コマンド種別
                              0      ：コマンド送信のみ
                              1      ：リード系コマンド（※1）
                      bit0-2
                              2      ：ライト系コマンド（※2）
                              7      ：受信待ち時間指定
                              その他    ：将来のための予約
                              受信ゲインアップ
                                受信ゲインアップをおこなうか否かを指定します
                      bit3
                                0：無効
                                1：有効 （ライト系処理で推奨）
                              ハンドル自動付加
                                RF タグへの送信データに自動で Handle を
                      bit4      付加するか否かを指定します
                                0：付加する（※3）
   データ部
                1               1：付加しない
                              受信時 CRC 付加 （リーダライタ→上位機器）
                                RF タグから受信した CRC を、上位機器への
                      bit5      レスポンスに付加するか否かを指定します
                                0：付加する
                                1：付加しない
                              受信時 CRC チェック（RF タグ→リーダライタ）
                                RF タグから受信した CRC のチェックを、
                      bit6      リーダライタでおこなうか否かを指定します
                                0：おこなう
                                1：おこなわない
                              送信時 CRC 付加 （リーダライタ→RF タグ）
                                リーダライタから RF タグへのデータ送信時に、
                      bit7      CRC を付加するか否かを指定します
                                0：付加しない
                                1：付加する（※4）
  （次ページへ続く）


  （前ページからの続き）
   ラベル名      バイト数     内容
                      受信データビット長（1～2008）
                      RF タグから受信する全データビット長（Header から CRC まで）
                      を指定します。
                2
                      受信 bit 長を 2 バイトで表し、上位バイトを先にセットします。
                      コマンド送信のみの場合は[00 00]h を設定します。
                      ※最大 2008[bit]（＝251[byte]）まで受信可能
                      受信タイムアウト時間（msec）
                       受信タイムアウト時間を指定します。
                       コマンド種別=7（受信待ち時間指定）を指定した場合のみ、本フィ
               (2)     ールドを指定します。
                       RF タグの応答タイミングに合わせて、        1～20 の範囲で指定します。
                       その他の種別を指定した場合は省略します。
                       指定時間を 2 バイトで表し、上位バイトを先にセットします。
                      送信データビット長
                      RF タグへ送信するコマンドデータの有効ビット数を指定します。
                2
                      ※「ハンドル自動付加」=[付加する]の場合や、          「送信時 CRC」=[付
                        加する]の設定の場合は、それらのデータ長は含めません。
                      RF タグへ送信するコマンドデータ（1～247）
                      RF タグへ送信するコマンドデータをバイトデータとしてセットし
                n
                      ます。送信データビット長がバイト単位に収まらず端数 bit が生じ
                      る場合は、最終バイトの上位ビット側に詰めてセットします。
     ETX        1     03h
     SUM        1     SUM 値（ 「5.4 SUM の計算方法」参照）
      CR        1     0Dh
  ※1：レスポンス受信のタイムアウトの判定値として FLASH アドレス 93([5D]h)の「Read コマン
     ドタイムアウト時間」を使用します。
  ※2：レスポンス受信のタイムアウトの判定値として FLASH アドレス 91([5B]h)の「Write コマ
     ンドタイムアウト時間」を使用します。
  ※3：「ハンドル自動付加」の設定が[付加する]の場合、「リーダライタが内部で保持している
     Handle データ(16[bit])」を、「RF タグへ送信するコマンドデータ」の後に付加して RF タ
     グに送信します。
  ※4：「送信時 CRC 付加」の設定が[付加する]の場合、「RF タグへ送信するコマンドデータ」に
     対する「CRC 計算結果(16[bit])」を後ろに付加して RF タグに送信します。
     「ハンドル自動付加」の設定が[付加する]の場合は、「RF タグへ送信するコマンドデータ」
     に「Handle データ(16[bit])」を加えたデータに対して CRC 計算をおこない、Handle デー
     タの後ろに「CRC 計算結果(16[bit])」を付加して RF タグに送信します。


  [ACK レスポンス]
    ラベル名   バイト数                       内容
     STX      1       02h
    アドレス      1       00h（「5.2 通信フォーマットの詳細」参照）
    コマンド      1       30h（ACK）
    データ長      1       データ部のデータ長（1～255）
              1       FFh
                      動作パラメータ
                1
                      送信コマンドにセットした動作パラメータが返ります。
                2     受信データビット長（1～2008）
                      RF タグからの受信データ（1～251 バイト）
                      バイト単位でデータがセットされます。
                      受信データビット長が 8 の整数倍ではない場合、最下位バイトには
   データ部               無効なビットデータが含まれる可能性があります。
                      受信データビット長からデータの有効範囲を確認の上、有効なデー
                      タだけを抜き出して使用してください。
                n
                      最下位バイトの有効ビット数が端数ビットの場合、有効データは上
                      位ビット側に詰めてセットされます。
                      ※RF タグからのレスポンスはビット単位のパラメータとなってお
                        り、通常は先頭１ビットに Header がセットされますので、その
                        後に続くデータの解析はビットシフトなどの処理をおこなう必要
                        があります。
     ETX        1     03h
     SUM        1     SUM 値（「5.4 SUM の計算方法」参照）
      CR        1     0Dh


［NACK レスポンス］
 「7.6 NACK レスポンスとエラーコード」参照。


 ［コマンド＆レスポンス例］

  (例 1) ISO/IEC 18000-63 規格で規定された、[Read]コマンドを、[UHF_ThroughCmd]を
       使用して実装する場合
      ・User 領域の Word アドレス[00]h から 1[Word]を読み取りし、[0000]h が返った場合
    ● コマンド
       [TX] 02 00 55 0A FF 81 00 31 00 1A C2 C0 00 40 03 F1 0D
    ● レスポンス
       [RX] 02 00 30 0B FF 81 00 31 <TAG_RESPONSE_BITS_BYTES> 03 9D 0D


  ●参考資料 ISO18000-63 規格の抜粋（要約）
 ＜Read Command＞
     項目       Command           MemBank         WordPtr     WordCount    RN16    CRC16
    bit 長            8              2              8            8         16       16
                                                開始 Word      読み取り
     定義             [C2]h      [11]b=User                               Handle   CRC-16
                                                アドレス         Word 数
                    [C2]h         [11]b           [00]h       [01]h      自動       自動
   コマンド
              1100 0010             11          0000 0000   0000 0001    付加       計算

  ・送信データビット長 = 8+2+8+8 = 26 [bit]となります。
   ※RN16 の 16[bit]は、「ハンドル自動付加」=[付加する]の設定のため、加算しません。
   ※CRC16 の 16[bit]は、「送信時 CRC 付加」=[付加する]の設定のため、加算しません。
  ・RF タグへ送信するコマンドデータは、byte 単位(1[byte]=8[bit])で指定します。
   不足分は下位ビットに[0]埋めします。上記 26 [bit]に 6[bit]の[00 0000]を付加して、
   [1100 0010 1100 0000 0000 0000 0100 0000]b = [C2 C0 00 40]h となります。

＜Read Command の成功時のレスポンス＞
   項目       Header          Memory Words           RN16      CRC16
  bit 長       1                 Variable             16        16
                             読み取りデータ
   定義        [0]b                                 Handle     CRC-16
                            1[Word] = 16[bit]

  ・受信データビット長 = 1+16+16+16 = 49 [bit]となります。


    ● コマンド
      [TX] 02 00 55 0A FF 81 00 31 00 1A C2 C0 00 40 03 F1 0D

        ・動作パラメータ：[81]h (= [1000 0001]b)
          bit2-0 「コマンド種別」              [001: リード系コマンド]
          bit3   「受信ゲインアップ」            [0: 無効]
          bit4   「ハンドル自動付加」            [0: 付加する]
          bit5   「受信時 CRC 付加」          [0: 付加する]
          bit6   「受信時 CRC チェック」 [0: おこなう]
          bit7   「送信時 CRC 付加」          [1: 付加する]
        ・受信データビット長：49 [bit] = [00 31]h
        ・送信データビット長：26 [bit] = [00 1A]h
        ・RF タグへ送信するコマンドデータ：[C2 C0 00 40]h

    ● レスポンス
      [RX] 02 00 30 0B FF 81 00 31 <TAG_RESPONSE_BITS_BYTES> 03 9D 0D

        ・動作パラメータ：[81]h (コマンドにセットした値がそのままセットされる)
        ・受信データビット長：[00 31]h = 49 [bit]
        ・RF タグからの受信データ：[<TAG_RESPONSE_BITS_BYTES>]h

        ＜RF タグからの受信データの内訳＞
        ・受信データの先頭 1[bit]に Header (=[0]b)が含まれているため、
         1[bit]論理左シフトします。
         [<TAG_RESPONSE_BITS_BYTES>]h << 1 = [<TAG_RESPONSE_BITS_BYTES>]h
              ・MemoryWord         = [00 00]h
              ・RN16               = [92 82]h
              ・CRC16              = [29 1D]h
          ※受信データビット長=49[bit]のため、下位 7[bit]に[000 0000]b が付加されています。
           1[bit]論理左シフトにより、さらに下位 1[bit]に[0]b が付加されるため、最下位の
           1[byte] (=8[bit])は無効な bit となります。


  (例 2) ISO/IEC18000-63 規格で規定された、[BlockWrite]コマンドを、
       [UHF_ThroughCmd]を使用して実装する場合
       ・User 領域の Word アドレス[00]h から 1[Word]に[0000]h を書き込む場合
    ● コマンド
       [TX] 02 00 55 0C FF 8A 00 21 00 2A C7 C0 00 40 00 00 03 01 0D
    ● レスポンス
       [RX] 02 00 30 09 FF 8A 00 21 <TAG_RESPONSE_BITS_BYTES> 03 8A 0D

●参考資料 ISO18000-63 規格の抜粋（要約）
 ＜BlockWrite Command＞
   項目     Command     MemBank      WordPtr       WordCount      Data        RN16     CRC16
  bit 長       8           2           8                8      Variable       16        16
                                   開始 Word           読み取り     書き込み         RF タグの
   定義       [C7]h     [11]b=User                                                     CRC-16
                                   アドレス              Word 数    データ          Handle
                                                              0000 0000
  コマンド    1100 0111      11        0000 0000     0000 0001                 自動付加      自動計算
                                                              0000 0000

  ・送信データビット長 = 8+2+8+8+16 = 42 [bit]となります。
   ※RN16 の 16[bit]は、「ハンドル自動付加」=[付加する]の設定のため、加算しません。
   ※CRC16 の 16[bit]は、「送信時 CRC 付加」=[付加する]の設定のため、加算しません。
  ・RF タグへ送信するコマンドデータは、byte 単位(1[byte]=8[bit])で指定します。
   不足分は下位ビットに[0]埋めします。上記 42 [bit]に 6[bit]の[00 0000]を付加して、
   [1100 0111 1100 0000 0000 0000 0100 0000 0000 0000 0000 0000]b
   = [C7 C0 00 40 00 00]h となります。

 ＜BlockWrite Command の成功時のレスポンス＞
   項目      Header       RN16        CRC16
  bit 長       1          16           16
                      RF タグの
   定義         0                    CRC-16
                       Handle

  ・受信データビット長 = 1+16+16 = 33 [bit]となります。


    ● コマンド
      [TX] 02 00 55 0C FF 8A 00 21 00 2A C7 C0 00 40 00 00 03 01 0D
        ・動作パラメータ：[8A]h (= [1000 1010]b)
          bit2-0 「コマンド種別」             [010: ライト系コマンド]
          bit3   「受信ゲインアップ」           [1: 有効]
          bit4   「ハンドル自動付加」           [0: 付加する]
          bit5   「受信時 CRC 付加」         [0: 付加する]
          bit6   「受信時 CRC チェック」 [0: おこなう]
          bit7   「送信時 CRC 付加」         [1: 付加する]
        ・受信データビット長：33 [bit] = [00 21]h
        ・送信データビット長：42 [bit] = [00 2A]h
        ・RF タグへ送信するコマンドデータ：[C7 C0 00 40 00 00]h

    ● レスポンス
      [RX] 02 00 30 09 FF 8A 00 21 <TAG_RESPONSE_BITS_BYTES> 03 8A 0D
        ・動作パラメータ：[8A]h (コマンドにセットした値がそのままセットされる)
        ・受信データビット長：[00 21]h = 33 [bit]
        ・RF タグからの受信データ：[<TAG_RESPONSE_BITS_BYTES>]h

        ＜RF タグからの受信データの内訳＞
        ・受信データの先頭 1[bit]に Header (=[0]b)が含まれているため、
         1[bit]論理左シフトします。
         [<TAG_RESPONSE_BITS_BYTES>]h << 1 = [<TAG_RESPONSE_BITS_BYTES>]h
              ・RN16 = [8C 92]h
              ・CRC16 = [38 EF]h
          ※受信データビット長=33[bit]のため、下位 7[bit]に[000 0000]b が付加されています。
           1[bit]論理左シフトにより、さらに下位 1[bit]に[0]b が付加されるため、最下位の
           1[byte](=8[bit])は無効な bit となります。


  (例 3) Impinj 社の RF タグ Chip M730 のカスタムコマンドの[Margin Read]コマンドを、
       [UHF_ThroughCmd]を使用して実装する場合
       ・EPC 領域のビットアドレス[20]h から 96[bit]に[<TAG_MASK_BYTES>]h が
       書かれた RF タグに対して[Margin Read]コマンドを実行する場合
    ● コマンド
       [TX] 02 00 55 17 FF 81 00 21 00 82
            <TAG_MASK_BYTES> 03 72 0D
    ● レスポンス
       [RX] 02 00 30 09 FF 81 00 21 <TAG_RESPONSE_BITS_BYTES> 03 03 0D

●参考資料 Impinj 社 M730 のデータシートの[Margin Read]コマンドの抜粋（要約）
＜MarginRead Command＞
    項目       Command       MemBank        BitPtr         Length      Mask         RN16       CRC16
   bit 長         16            2            8              8        Variable       16           16
                                        開始ビット
    定義        [E0 01]h    [01]b=EPC                      ビット数       マスク値         Handle      CRC-16
                                         アドレス
                                                                      以下           自動          自動
  コマンド        [E0 01]h       [01]b         [20]h         [60]h
                                                                      参照           付加          計算

  ※マスク値は 96[bit]で、[<TAG_MASK_BYTES>]h
  ・送信データビット長 = 16+2+8+8+96 = 130 [bit]となります。
   ※RN16 の 16[bit]は、「ハンドル自動付加」=[付加する]の設定のため、加算しません。
   ※CRC16 の 16[bit]は、「送信時 CRC 付加」=[付加する]の設定のため、加算しません。

  ＜送信コマンド列の組み立て方法＞
  (1)Command は[E0 01]h をそのまま使用します。
  (2)MemBank=[01]b の 2[bit]は、6[bit]の[00 0000]b を下位に付加して、[0100 0000]b=[40]h
  (3)上記以降は、2[bit]論理右シフトします。
    [20 60 <TAG_MASK_BYTES>]h >> 2 = [08 18 38 A0 04 64 69 40 C0 18 50 40 00 0C 40]h
  (4) (3)の先頭バイトに(2)を加算し([08]h + [40]h = [48]h)、その結果の先頭に(1)を付加します。
       → 送信コマンド列 = [<TAG_MASK_BYTES>]h

＜MarginRead Command の成功時のレスポンス＞
   項目        Header        RN16         CRC16
   bit 長        1            16            16
   定義           0          Handle       CRC-16

  ・受信データビット長 = 1+16+16 = 33 [bit]となります。


    ● コマンド
      [TX] 02 00 55 17 FF 81 00 21 00 82
           <TAG_MASK_BYTES> 03 72 0D
        ・動作パラメータ：[81]h (= [1000 0001]b)
          bit2-0 「コマンド種別」              [001: リード系コマンド]
          bit3   「受信ゲインアップ」            [0: 無効]
          bit4   「ハンドル自動付加」            [0: 付加する]
          bit5   「受信時 CRC 付加」          [0: 付加する]
          bit6   「受信時 CRC チェック」 [0: おこなう]
          bit7   「送信時 CRC 付加」          [1: 付加する]
        ・受信データビット長：33 [bit] = [00 21]h
        ・送信データビット長：130 [bit] = [00 82]h
        ・RF タグへ送信するコマンドデータ：[<TAG_MASK_BYTES>]h

    ● レスポンス
      [RX] 02 00 30 09 FF 81 00 21 <TAG_RESPONSE_BITS_BYTES> 03 03 0D
        ・動作パラメータ：[81]h (コマンドにセットした値がそのままセットされる)
        ・受信データビット長：[00 21]h = 33 [bit]
        ・RF タグからの受信データ：[<TAG_RESPONSE_BITS_BYTES>]h

        ＜RF タグからの受信データの内訳＞
        ・受信データの先頭 1[bit]に Header (=[0]b)が含まれているため、
         1[bit]論理左シフトします。
         [<TAG_RESPONSE_BITS_BYTES>]h << 1 = [<TAG_RESPONSE_BITS_BYTES>]h
              ・RN16 = [EA 45]h
              ・CRC16 = [22 F9]h
          ※受信データビット長=33[bit]のため、下位 7[bit]に[000 0000]b が付加されています。
           1[bit]論理左シフトにより、さらに下位 1[bit]に[0]b が付加されるため、最下位の
           1[byte](=8[bit])は無効な bit となります。
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
| 成功ACK例 | `02 00 30 01 FF 03 35 0D` |
| ACKデータ部の先頭 | `FFh` |
| 注意 | タグメモリ操作は、Select/Query/Access/Write/Lock/Kill等の内部処理結果によりNACKになる場合があります。ここに示すHexは正常終了時のACK例であり、実行可否や対象タグ条件を省略してよいという意味ではありません。成功ACKだけでなく、NACKのエラーコード1/2を必ず解析してください。 |

### 8.2 NACK例（フォーマットエラーの例）

| 項目 | 内容 |
|---|---|
| 代表NACK Hex | `02 00 31 0A FF 44 00 00 00 00 00 00 00 00 03 83 0D` |
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
| `CMD=30h` かつ `DATA[0]` が `FFh` またはPDF該当節の応答識別子 | `ACK` | 対象コマンド `55h FFh` の成功応答としてPDF該当節を読む |
| `CMD=6Ch` | `RF_TAG_DATA` | 自動読み取り中の非同期応答候補。通常ACKとは分離する |
| `CMD=30h` の後にタグ状態確認が必要 | `ACK_PENDING_TAG_VERIFY` | タグメモリ操作はACKだけで業務成功と断定しない |

対象識別子: コマンド `55h` / 詳細 `FFh` / サブ `なし`。


#### ACK/データ部offset
成功ACK `CMD=30h` のDATA先頭は、原則として `FFh` またはPDF該当節の応答識別子として扱います。

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
| 0 | `error_source` | 原則として対象コマンドの詳細識別子。対象: `55h FFh` |
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
