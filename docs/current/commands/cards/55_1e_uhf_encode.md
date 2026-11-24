---
title: "UHF_Encode"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.5.10"
command_group: "rf_tag_communication"
command_name: "UHF_Encode"
command_byte: "55h"
detail_command: "1Eh"
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
  - "55_1e_uhf_encode_raw.md"
  - "55_1a_uhf_block_write.md"
  - "55_18_uhf_lock.md"
  - "55_33_03_write_access_password.md"
  - "55_15_uhf_read.md"
  - "../../RAM_FLASH_IMPACT_MATRIX.md"
  - "../../SOURCE_REVIEW_STATUS.md"
  - "../../RF_SAFETY_AND_CARRIER_RULES.md"
tags:
  - "utr-s201"
  - "command-card"
  - "rf-tag-communication"
  - "rf-emission"
  - "write-operation"
  - "tag-memory"
  - "requires-antenna"
  - "requires-tag"
  - "specification-reference"
  - "access-password"
  - "uhf-encode"
---

# UHF_Encode（エンコード）
## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **UHF_Encode** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.5.10`
- コマンド分類: rf_tag_communication
- 確認区分: `tag-memory-or-high-impact`
- 操作レベル: write/configuration
- コマンドバイト: `55h` / 詳細コマンド: `1Eh` / サブコマンド: `null`
- 確認状態: `SPECIFICATION_REFERENCE`
- 結果状態: `NOT_AN_EXECUTION_RESULT`

本カードは仕様参照資料です。PDFを期待結果の基準とし、実機試験の実施結果とは区別します。[確認状態索引](TEST_STATUS_INDEX.md)を参照してください。

## 2. 目的

Reserved・EPC/UII・Userの複数領域への書込みと、任意のLock処理を一括で要求します。リーダライタのAccessパスワードも内部で変更するタカヤ独自の複合コマンドです（p.291）。

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

出典: Ver.1.17 §7.5.10 p.291–305、§7.6 p.316–318。[原典転記](55_1e_uhf_encode_raw.md)は保持し、ここでは要求の組立てと条件を整理します。2026-09-09～10の部分照合であり、全機種・ROMの適合や実機試験を示しません。

### 6.1 flags（DATA[1]）

DATA[0]は詳細1Eh。p.291・294のflagsは以下の通りです。

| bit | 0 | 1 |
|---|---|---|
| 0 | RF側Writeを使用 | RF側BlockWriteを使用 |
| 1 | 実行前のリーダ側Accessパスワードを保持しない | 保持する |
| 2 | Reserved書込み前のAccess発行を指定しない | 指定する |
| 3 | EPC/UII書込み前のAccess発行を指定しない | 指定する |
| 4 | User書込み前のAccess発行を指定しない | 指定する |
| 5～7 | 予約。通常0 | 機能を割り当てない |

bit0はどちらもRF側で1 Wordずつ書き込みます。BlockWrite2の一括Word送信とは異なり、途中失敗のNACKでも一部書込み済みの場合があります。BlockWriteはタグのオプションコマンドのため、タグの対応を確認します。

### 6.2 各bankの可変領域

p.292。要求内の並びはReserved（00）→EPC/UII（01）→User（11）で固定です。bank番号を送る欄やTID書込み枠はありません。各枠は、1 byteの長さLに続けてL byteの内容を置きます。

| 条件 | 長さL | 後続の内容 |
|---|---|---|
| 書き込まない | 0 | 開始位置もデータも省略。長さ欄自体は残る |
| n Word書き込む | 2n+2 | 2 byteの開始Wordアドレス（MSB先行）、2n byteの書込みデータ |

長さ欄はWord数そのものではありません。非ゼロLからはn=(L−2)/2を得ます。記載上限は各bank最大123 Wordですが、全枠とLockを含めたLEN上限を同時に満たす必要があります。L=2の0 Word書込みの意味は未確認で、書込み省略の0と同一視しません。

### 6.3 DATA内の位置と全体長

p.291–294。Lr・Le・Luは各bankの長さ欄の値、LkはLock長です。すべてDATA先頭を0とするoffsetです。

| offset | 内容 |
|---|---|
| 0 | 詳細1Eh |
| 1 | flags |
| 2 | Lr |
| 3～2+Lr | Reserved内容（Lr=0なら存在しない） |
| 3+Lr | Le |
| 4+Lr～3+Lr+Le | EPC/UII内容（Le=0なら存在しない） |
| 4+Lr+Le | Lu |
| 5+Lr+Le～4+Lr+Le+Lu | User内容（Lu=0なら存在しない） |
| 5+Lr+Le+Lu | Lk |
| 6+Lr+Le+LuからLk byte | Lockパラメータ（Lk=0なら存在しない） |

LEN=6+Lr+Le+Lu+Lkで最大255 byte、総フレーム長はLEN+7で最大262 byteです。固定6 byteは詳細・flags・4つの長さ欄であり、長さ欄を再加算しません。

### 6.4 長さの境界例

p.294の式からの算術整理です。タグ自体の容量・書込み可否とは別に確認します。

| 書込み範囲 | Lk | LEN |
|---|---|---|
| 1 bankだけ123 Word | 0 | 6+248=254 |
| 1 bankだけ123 Word | 3 | 257となり指定不可。Lockありでは122 Wordまで |
| Reserved 4 Word・EPC/UII 7 Word・User 109 Word | 3 | 6+10+16+220+3=255（原典の最大例） |

すべての長さ欄を0にした要求やLockだけの要求について、長さの計算結果だけで実行可否を確定しません。

### 6.5 Lock情報

p.293–294・299。Lk=00hはLockなしで後続3 byteを省略、03hはLockありでパラメータ1～3を付けます。01hを単なるON指定として使いません。

3 byteの各Mask／Actionは[Lockカード](55_18_uhf_lock.md)の10組と同じ配置です（p.279とp.293）。パラメータ3のbit0～3は0固定。Passwordの設定／解除とPermaLockの恒久化を区別します。TIDのLock対象があることは、EncodeにTID書込み枠があることを意味しません。

PermaLockのp.227の包括的な説明は[OPEN-014](../../SOURCE_REVIEW_STATUS.md)で訂正確認待ちです。Encodeを恒久ロック解除の手段にしません。

## 7. 実行条件と状態の変化

公式PDF掲載例は仕様説明であり、そのまま実機へ送る許可ではありません。原典転記内のマスク済み例は実行可能なフレームではなく、置換後のSUMとして使用できません。実機送信用の値・完成Hexは対象、範囲、停止・復旧条件を確認してから扱います。

### 7.1 Access発行の選択

p.297–298。Password Write LockまたはPassword Read/Write Lockが掛かった書込み対象には、一致するAccessパスワードによる認証が必要です。flagsのbit2～4でbankごとに発行を指定します。複数bankを指定しても認証は最初の1回で、Secured状態になった後の書込み・Lockでは再発行不要と説明されています。

p.297のフローは、非ゼロのタグAccessパスワードを書き込む場合にReservedを先に確認し、その後EPC/UII→User→Reservedの順で最初に必要なAccess指定を選びます。ゼロ指定またはAccess領域を書かない場合はEPC/UIIから確認します。未ロック領域の書込みに一律で発行を強制しません。

### 7.2 認証で使用するパスワード

| 処理 | 原典の説明 |
|---|---|
| Reserved書込み前のAccess | 実行時のリーダ側設定。事前に[Access設定](55_33_03_write_access_password.md)で書く（p.298） |
| EPC/UII・User書込み、LockのAccess | 要求でAccess領域（Reserved Word 02h・03h）を書き込むならその値、書かないならリーダ側設定（p.298–299） |

後者の説明にはゼロ書込み時の例外が明記されていません。一方p.299はゼロでAccess発行不可として処理順を変更し、p.305例2は既存の非ゼロパスワードを前提にしています。ゼロ化前の認証値の説明は[OPEN-018](../../SOURCE_REVIEW_STATUS.md)で確認待ちです。要求のゼロを先に認証値へ設定する手順は確定しません。

`requires_access_password: true`は、この条件と実行後の保持値を確認する意味です。全Encodeで実行前に非ゼロ値が必須という意味ではありません。p.304例1は、事前値ゼロ・未ロックのタグに新しいパスワードを書いてLockする例です。

### 7.3 要求内の並びと内部処理順

p.299では、タグAccessパスワードへの書込み値によって、次の順序を定義します。要求内のbank順は§6.2のままです。

| タグAccessパスワードへの指定 | 内部処理順 |
|---|---|
| 非ゼロを書き込む | Reserved→EPC/UII→User→Lock→リーダ側パスワードの終了処理 |
| ゼロを書き込む | EPC/UII→User→Lock→Reserved→リーダ側パスワードの終了処理 |

各処理の有無は要求の各長さ欄で指定します。Access領域を書かない場合の完全な処理順、2 Wordの一部だけを書き換える場合の新パスワード合成は未確認です。p.297のAccess選択フローを、そのまま全内部処理の順序とみなしません。

### 7.4 ACK後のリーダ側パスワード

p.295。旧値は実行前のリーダ側Access設定、新値はタグAccess領域へ書く2 Wordを表します。

| 保持bit1 | タグAccess領域への書込み | 終了後のリーダ側設定 |
|---|---|---|
| 1（保持する） | あり／なし | 旧値 |
| 0（保持しない） | あり | 新値 |
| 0（保持しない） | なし | ゼロ |

保持する対象はリーダ側設定です。タグの変更は取り消されません。タグのパスワードを変更して旧値を保持すると、同じタグへの後続Read等で不一致になり得ます。保持しない場合も、Access領域を書かずACKになればリーダ側は旧値ではなくゼロになります。

### 7.5 NACK後のリーダ側パスワード

p.296。NACKでも終了時の設定は次のように分かれます。

| 保持bit1 | タグAccess領域への書込み指定／進行状況 | 終了後のリーダ側設定 |
|---|---|---|
| 1 | すべて | 旧値 |
| 0 | あり、Reserved書込み成功 | 新値 |
| 0 | あり、Reserved書込み失敗または実行前に失敗 | 旧値 |
| 0 | なし | 旧値 |

これはリーダ側設定の規則です。Reservedの途中失敗ではタグの一部が変更済みの可能性があり、旧値へ戻ったことからタグとの一致を保証しません。ホストTIMEOUTでは応答を確認できないため、ACK／NACKのどちらかや終了処理完了を推測しません。

### 7.6 キャリア・ハンドルと対象

p.302。実行前がキャリアON維持なら、保持中のハンドルを使用し、未保持ならQ=0のInventoryで取得します。終了後もON維持です。実行前がOFFなら内部でONにし、Q=0で取得したハンドルを処理中維持し、終了時にOFFへ戻してハンドルを破棄します。

単一の対象タグを維持する条件は[BlockWrite](55_1a_uhf_block_write.md)・[Lock](55_18_uhf_lock.md)も確認します。対象の同定、Select条件、キャリア維持を確認し、EPC変更後に旧EPCだけで同じタグを再選択できると仮定しません。キャリアの復帰とタグメモリの巻戻しは別です。

### 7.7 掲載例の不一致（訂正未確定）

p.305例2の2点は[OPEN-017](../../SOURCE_REVIEW_STATUS.md)へ記録しました。原典転記は変更せず、訂正案の確定を保留します。

| 箇所 | 原典の記載 | 訂正案と根拠 |
|---|---|---|
| 上段表のLock処理内容 | 88 00 00 | 28 00 00。同ページ下段のbit3・bit5のMask表と送信例が28 |
| 最終行の実行後リーダ側パスワード | 実行前の非ゼロ値 | ゼロ。保持bit1=0でタグAccess領域をゼロへ書き、ACKとなる条件はp.295の新値保持に該当 |

「全MemBankを0に戻す」という冒頭も、掲載要求の指定範囲を超える消去やTID書換えの保証として使いません。115ms対261ms（p.303）はMonza4QTでの原典例であり、全タグの時間保証・ホストtimeout値・本整備の測定結果ではありません。

## 8. AI実装用レスポンス定義

### 8.1 固定長ACK

p.300。共通フレームの検査後、CMD=30h・LEN=01h・DATA[0]=1Ehをすべて照合します。総長は8 byteです。p.304–305の掲載ACK例は `02 00 30 01 1E 03 54 0D` です。

DATA[1]以降のpayloadはありません。bankごとの成否、成功Word数、書込み値、最終Lock状態、リーダ側パスワードは返りません。内部BlockWriteやLockのACKを上位へ順次返す形式ではありません。自動読み取り用の完了通知OFFを、このACKの省略条件にしません。ADRもRFタグデータ用のアンテナIDへ読み替えません。

### 8.2 NACKと失敗箇所

p.300・316–318。CMD=31h・LEN=0Ah、総17 byte。DATA[0]は詳細1Eh、DATA[1]はコード1、DATA[2]はコード1=0Ahの場合のコード2です。共通値は[応答マスタ](../../RESPONSE_AND_NACK_MASTER.md)へ進みます。

| DATA[3]（コード3） | 失敗箇所 |
|---|---|
| 01h | Reserved書込み |
| 02h | EPC/UII書込み |
| 03h | User書込み |
| 05h | Lock発行 |

コード3はフレームoffset 7、原典の数え方では8 byte目です。04hは未定義で、成功Word数や失敗Word位置でもありません。DATA[4]のコード4をBlockWrite2と同じ追加エラーとして解釈しません。DATA[5～9]の予約は非ゼロでも意味を補わず、SUMには受信値を含めます。

### 8.3 判定・確認手順

1. 共通フレームの総長・固定値・SUMを検査し、要求の詳細と応答を照合する。
2. 固定ACKならコマンド正常終了を記録し、業務上の確認とは分ける。無関係な通知は要求成功にしない。
3. NACKならコード1／条件付きコード2／コード3を保持し、§7.3の処理順と§7.5を併せて確認する。未知の値にも独自の段階を割り当てない。
4. 同じコード3=02hでも、非ゼロパスワード書込みならReserved後、ゼロ書込みならReserved前の失敗である。コード値を固定の進捗順として扱わない。
5. TIMEOUTでは未変更・復帰済みと断定せず、停止条件に従う。部分書込み・パスワード変化・Lockを確認せず同じ要求を自動再送しない。

読戻しは対象・認証・Lockの条件を確認して計画します。[Read](55_15_uhf_read.md)は1回最大32 Wordのため長い領域は分け、読取り不可の秘密領域やLock状態を単純な値の読戻しで確認できる前提にしません。リーダ側Access設定も読戻し不可です。これらは仕様から導く確認設計であり、実機で検証した結果ではありません。

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
- [55_1e_uhf_encode_raw.md](55_1e_uhf_encode_raw.md)
- [55_1a_uhf_block_write.md](55_1a_uhf_block_write.md)
- [55_18_uhf_lock.md](55_18_uhf_lock.md)
- [55_33_03_write_access_password.md](55_33_03_write_access_password.md)
- [55_15_uhf_read.md](55_15_uhf_read.md)
- [RAM_FLASH_IMPACT_MATRIX.md](../../RAM_FLASH_IMPACT_MATRIX.md)
- [SOURCE_REVIEW_STATUS.md](../../SOURCE_REVIEW_STATUS.md)
- [RF_SAFETY_AND_CARRIER_RULES.md](../../RF_SAFETY_AND_CARRIER_RULES.md)


PDF原本は社内の正式な管理場所から別途準備してください。GitHubにはPDF原本をアップロードしないでください。
