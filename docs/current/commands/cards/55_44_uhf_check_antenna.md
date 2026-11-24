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
requires_parameters: true
verification_status: "SPECIFICATION_REFERENCE"
result_status: "NOT_AN_EXECUTION_RESULT"
related_docs:
  - "../../COMMAND_MASTER_V117.md"
  - "../../TRACEABILITY_INDEX_V117.md"
  - "../../RESPONSE_AND_NACK_MASTER.md"
  - "../../DEVICE_ROM_IDENTIFICATION_AND_SUPPORT.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
  - "../../PARAMETER_CONFIRMATION_GUIDE.md"
  - "../../AI_IMPLEMENTATION_GUARDRAILS.md"
  - "4f_80_read_error_info.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "../../ANTENNA_NUMBERING_SCHEMES.md"
  - "4e_00_10_write_reader_mode.md"
tags:
  - "utr-s201"
  - "command-card"
  - "reader-control"
  - "rf-emission"
  - "requires-antenna"
  - "specification-reference"
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
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

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
| パラメータ確認 | 機種別のアンテナ番号を確認 |
| 明示許可 | RF診断が許可された範囲で実行 |

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

公式PDF掲載の完成Hex例は仕様説明として記載します。実機へそのまま送信する許可ではありません。`<...>` を含むマスク例・構造例は実行可能なフレームではなく、掲載SUMも置換後の値として使えません。

利用者の条件に合わせた送信用HexやSUM計算済みコマンドは、対象・値・影響範囲・停止・復旧条件を確認してから扱います。安全ガードを省略した実装コードは記載しません。

AIに実装を依頼する場合は、まずフレーム生成、SUM計算、送信、受信、ACK/NACK解析、timeout処理を分けて設計してください。

## 8. 指定端子の接続診断

### 8.1 要求と固定ACK

要求はCMD=55h・LEN=02h、DATA[0]=44h・DATA[1]=アンテナ番号で総9 byteです（p.137）。成功ACKはCMD=30h・LEN=03h、DATA[0]=44h・DATA[1]=アンテナ番号・DATA[2]=接続情報で総10 byteです（p.138）。フレーム長・SUM、詳細と要求番号への対応を確認します。

このACKは固定3 byteのDATAで、RFタグのEPC/UII・読取枚数・完了通知を含みません。アンテナID出力ONでもADRへ診断番号を移さず、番号はDATA[1]から読みます。TID付加や自動読み取りの通知設定によって応答長・後続完了ACKが変わるという既存の汎用説明は適用しません。

### 8.2 機種別番号

| 機種 | 要求・ACKの番号値 | 端子表示 |
|---|---|---|
| UTR-S201／UTR-SHR201 | 00hのみ | ANT0 |
| UTR-SUN02-4CH | 00h～03h | ANT0～ANT3 |
| UTR-SUN02V-8CH／UTR-SUN02-8CH | 00h～07h | ANT1～ANT8 |

p.137–139の対応です。8CHのANT8は07h、4CHのANT3は03hです。機種を問わず表示番号をそのまま送信値にしません。本要求には外部アンテナ番号欄・全端子一括マスク・RAM/FLASH選択欄はありません。[番号体系](../../ANTENNA_NUMBERING_SCHEMES.md)に従い、RFタグ応答のADRや外部ユニット番号を流用しません。

### 8.3 ACK内の接続情報

| DATA[2] | p.138–139の意味 | 扱い |
|---|---|---|
| 00h | 接続OK、マッチング良好 | 指定端子の診断結果 |
| 01h | 未接続またはマッチングの極端なずれ等 | 接続エラーを示すACK |
| 02h | 存在しないアンテナ番号 | パラメータ異常を示すACK |

01h・02hもCMD=30hのACK内の結果で、NACKへ置換しません。02hをタグ0枚やLBTエラーと解釈せず、存在しない番号を検出するための無差別送信もしません。未定義結果値は元値を記録して未確認とし、正常へ丸めません。別途CMD=31hが来た場合は§7.6のNACKとして扱います。

### 8.4 RFと診断の限界

断線確認はキャリアセンス後にRFを出力し、反射電力から判断します（p.48–49）。タグは不要ですがRFを使うため、機種・ROM・対象端子・接続アンテナ・周波数・出力・地域・停止方法と送信許可範囲を確認します。受動的な配線読取りではありません。

01hはケーブル断線だけを断定せず、水分・人体・金属等によるマッチング悪化も確認します（p.139）。長いケーブルでは損失により実際の故障を断線として検知しない場合があります（p.48）。00hでもケーブル・全アンテナの完全な健全性、タグの存在や読取性能までは保証しません。

ROM 2.030以降は正常と判断されたポートではRFを出力でき、1.120以前のUTR-S201では断線判断中に全ポートで出力できないという違いがあります（p.49）。[エラー情報読取り](4f_80_read_error_info.md)は別の状態取得で、結果形式・取得時点を分けます。診断のために以前の状態が保持されると仮定しません。

### 8.5 モード・復旧・未確認範囲

本要求は連続65h／66h中の受付例外ではなく、動作保証外です（p.19–20）。00hへの復帰条件を確認してから診断します。RF診断後の選択アンテナ、キャリア状態、外部ユニット側の選択・診断範囲、出力時間と最長応答時間は本節だけでは確定できません。元の設定保持や自動RF停止を保証せず、必要な状態確認と復旧を計画します。

NACK・timeout・不正フレームは接続情報00h／01h／02hと別に記録します。受信できないことを未接続と断定したり、自動再送・出力増加・別端子への切替を追加したりしません。複数端子を診断する場合も機種に存在する各端子の結果を個別に記録し、単一端子の00hを全端子正常へ広げません。

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

- `4f_80_read_error_info.md`
- `../../SOURCE_REVIEW_STATUS.md`
- `../../ANTENNA_NUMBERING_SCHEMES.md`
- `4e_00_10_write_reader_mode.md`

PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
