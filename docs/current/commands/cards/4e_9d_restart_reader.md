---
title: "リスタート"
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: "7.3.10"
command_group: "reader_control"
command_name: "リスタート"
command_byte: "4Eh"
detail_command: "9Dh"
subcommand: null
operation_profile: "needs-metadata-confirmation"
operation_level: "reader-control"
rf_emission: false
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: false
requires_parameters: false
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
  - "reader-control"
  - "restart"
  - "no-response-success"
  - "pass-with-notes"
---

# リスタート

## 1. コマンドの位置づけ

このカードは、UTR-S201 シリーズ通信プロトコル説明書 Ver.1.17 に記載された **リスタート** を、AIとの実装・レビュー・検証で参照しやすくするための整理資料です。

- PDF章番号: `7.3.10`
- コマンド分類: リーダライタ制御
- 確認区分: `needs-metadata-confirmation`
- 操作レベル: リーダライタ制御
- コマンドバイト: `4Eh` / 詳細コマンド: `9Dh` / サブコマンド: `null`
- 確認状態: `REAL_DEVICE_VERIFIED_WITH_NOTES`
- 結果状態: `REAL_DEVICE_PASS_WITH_NOTES`

## 2. 目的

このコマンドの目的は、**リーダライタをリスタート（再起動）すること** です。

PDF 7.3.10では、リーダライタは本コマンドに対するACK/NACKを返しません。正常系でも「レスポンスなし」になるため、通常のACK待ち実装ではなく、送信後に約2秒以上待機し、ROMバージョン読み取りなどの低影響コマンドで復帰確認してください。

## 3. 使用可否・位置づけ

判定: `SUPPORTED`

このコマンドはPDF Ver.1.17のコマンド一覧に含まれるため、仕様上の対象コマンドとして扱います。

ただし、仕様に存在することと、実機へ送信してよいことは別です。実機送信前には、対象機種、ROMバージョン、接続先、パラメータ、影響範囲、復旧方法、停止条件を確認してください。

## 4. 安全性・影響分類

| 項目 | 判定 |
|---|---|
| RF送信 | なし |
| 書き込み操作 | なし |
| FLASH操作 | なし |
| タグメモリ操作 | なし |
| ROM確認 | あり |
| アンテナ条件確認 | なし |
| タグ条件確認 | なし |
| Accessパスワード確認 | なし |
| パラメータ確認 | なし |
| 明示許可 | 必要 |

高影響コマンドを、高影響という理由だけで仕様上禁止扱いにはしません。ただし、上記の確認事項が揃うまで実機送信しません。

## 5. 実装前の確認事項

実装前に、少なくとも以下を確認してください。

1. ROMバージョンを読み取り、シリーズ名と対象機種を確認する。
2. 対象コマンドが、その機種・ROMで利用可能か確認する。
3. このコマンドはACK/NACKを返さないため、無応答を即エラー扱いしない受信設計にする。
4. リスタート後、約2秒以上は次コマンドに応答できない前提で待機時間を設計する。
5. RAM上のコマンドモード用パラメータ、自動読み取りモード用パラメータがFLASH値で上書きされることを確認する。
6. 実行前に、必要なRAM設定スナップショットと復帰後の再設定要否を決める。
7. 復帰確認には、ROMバージョン読み取りなど低影響の読み取りコマンドを使う。

## 6. PDF仕様フィールド定義

以下は、公式PDF `7.3.10` のコマンド表、レスポンス表、条件、例を、AIがカード単体で参照できるように転記したものです。値一覧、byte数、条件、ACK/NACK条件を省略せず、この節を実装時の一次確認に使ってください。

```text
7.3.10 リスタート
 リーダライタをリスタート（再起動）するコマンドです。
 なお、リーダライタは本コマンドに対する応答を返しません。

   ［コマンド］
 ラベル名 バイト数                            内容
  STX    1         02h
 アドレス    1         00h（「5.2 通信フォーマットの詳細」参照）
 コマンド    1         4Eh
 データ長    1         01h
 データ部    1         9Dh（詳細コマンド）
  ETX    1         03h
  SUM    1         SUM 値（ 「5.3 SUM の計算方法」参照）
   CR    1         0Dh


［ACK レスポンス］
  リーダライタは応答を返しません。


［NACK レスポンス］
  リーダライタは応答を返しません。


［コマンド／レスポンス例］
   • コマンド
      02 00 4E 01 9D 03 F1 0D
     • レスポンス
        リーダライタは応答を返しません。

 ＜注意事項＞
  ・リーダライタは、リスタート実行後から約 2 秒間は、次のコマンドに応答できません。
   リスタート後に続けてコマンドを実行する場合には、2 秒以上の時間を空けてください。

   ・リスタートを実行すると、リーダライタの RAM に書かれた「コマンドモード用パラメータ」お
    よび「自動読み取りモード用パラメータ」はリセットされ、「FLASH データ」に書かれている
    値で上書きされます。
```

## 7. コマンド形式・PDFフィールド定義の読み方

この節は、PDF 7.3.10 のコマンド表・注意事項を、生成AIが実装に使える粒度へ分解したものです。このコマンドは、通常のACK/NACK待ちを行うコマンドではありません。

### 7.1 送信コマンドフレーム

| offset | フィールド | byte数 | 値 | 意味 |
|---:|---|---:|---|---|
| 0 | `STX` | 1 | `02h` | フレーム開始 |
| 1 | `ADR` | 1 | 通常 `00h` | リーダライタアドレス。共通通信フォーマットに従う |
| 2 | `CMD` | 1 | `4Eh` | リーダライタ制御コマンド |
| 3 | `LEN` | 1 | `01h` | DATA部は1byte |
| 4 | `DATA[0]` | 1 | `9Dh` | 詳細コマンド: リスタート |
| 5 | `ETX` | 1 | `03h` | フレーム終端 |
| 6 | `SUM` | 1 | `F1h` | PDF掲載例のSUM。`02+00+4E+01+9D+03 = F1h` |
| 7 | `CR` | 1 | `0Dh` | 改行終端 |

### 7.2 コマンド／レスポンス例

| 種別 | Hex / 内容 | 説明 |
|---|---|---|
| 送信例 | `02 00 4E 01 9D 03 F1 0D` | リーダライタへリスタートを要求 |
| レスポンス | なし | PDF上、ACKもNACKも返らない |

このコマンドでは、レスポンスなしが仕様上の正常系です。受信タイムアウトをそのまま通信失敗と決めつけず、「再起動中の無応答」と「送信失敗・未復帰」を分けて扱ってください。

### 7.3 リスタート後の待機と復帰確認

| 項目 | PDF仕様 / 実装判断 |
|---|---|
| ACK | 返らない |
| NACK | 返らない |
| 次コマンド応答不可時間 | リスタート実行後、約2秒間 |
| 復帰確認 | 2秒以上待ってからROMバージョン読み取りなど低影響コマンドで確認 |
| RAM設定への影響 | コマンドモード用RAMパラメータ、自動読み取りモード用RAMパラメータはリセットされ、FLASHデータの値で上書きされる |

### 7.4 設定・状態への影響

| 対象 | 影響 | 実装上の注意 |
|---|---|---|
| コマンドモード用RAMパラメータ | FLASHデータ値で上書き | 実行前にRAM設定スナップショットを保存し、復帰後に必要なら再設定する |
| 自動読み取りモード用RAMパラメータ | FLASHデータ値で上書き | 自動読み取り、アンテナ切替、TID付加、読取完了応答などの状態を再確認する |
| FLASHデータ | 直接書き換えない | 本コマンド自体はFLASH書き込みではないが、RAMはFLASH値へ戻る |
| RFキャリア・タグハンドル | 再起動により維持されない | 復帰後にキャリア状態、タグ通信前提を再取得する |
| シリアル接続 | 環境により一時的に無応答または再オープンが必要 | ポート維持に失敗した場合は、明示的に再接続してから復帰確認する |

### 7.5 実装ステップ

1. 実行前にROM/機種を確認する。
2. 必要なら現在のRAM設定スナップショットを取得する。
3. `02 00 4E 01 9D 03 F1 0D` の形でリスタートコマンドを送信する。
4. ACK/NACKを待って成功判定しない。
5. 約2秒以上待機する。
6. シリアルポートが無効化された場合は再オープンする。
7. ROMバージョン読み取りなど低影響コマンドで復帰確認する。
8. 実行前スナップショットと復帰後設定を比較し、RAM設定がFLASH値に戻ったことを前提に必要な再設定を行う。

## 8. レスポンス処理

レスポンス処理では、以下を区別してください。

- 仕様上の無応答
- 送信失敗
- 再起動待機中のtimeout
- 復帰確認コマンドのtimeout
- 復帰確認コマンドのACK/NACK
- ポート切断・再接続要求
- フレーム不正

### 8.1 受信分類ルール

| 条件 | 分類 | 実装アクション |
|---|---|---|
| リスタート送信直後にACK/NACKが来ない | `NO_RESPONSE_EXPECTED` | 正常系として扱い、約2秒以上待機する |
| リスタート送信自体が失敗 | `SEND_FAILED` | 再起動されたとは判断しない。ポート状態を確認する |
| 約2秒待機後、ROM読み取りが成功 | `RESTART_CONFIRMED` | 復帰成功。必要ならRAM設定を再取得・再設定する |
| 約2秒待機後、ROM読み取りがtimeout | `RESTART_CONFIRM_TIMEOUT` | 追加の高影響コマンドは送らず、接続・電源・ポートを確認する |
| 不完全フレームやノイズを受信 | `INVALID_FRAME_DURING_RESTART` | ACK成功とは扱わない。再同期またはポート再オープンを検討する |
| 復帰確認コマンドでNACK | `POST_RESTART_NACK` | リスタートACKではなく、復帰確認コマンドのNACKとして扱う |

対象識別子: コマンド `4Eh` / 詳細 `9Dh` / サブ `なし`。

### 8.2 ACK/レスポンス例

| 項目 | 内容 |
|---|---|
| 代表TX Hex | `02 00 4E 01 9D 03 F1 0D` |
| ACK | なし |
| NACK | なし |
| 正常判定 | 送信完了後、約2秒以上待ってから低影響コマンドで復帰確認 |

### 8.3 NACKの扱い

PDF 7.3.10では、本コマンドに対してNACKレスポンスも返しません。そのため、`CMD=31h` を本コマンド直後に受信した場合でも、まず以下を疑ってください。

| 受信内容 | 扱い |
|---|---|
| `CMD=31h` | リスタートコマンドの仕様上NACKではなく、送信前後に残っていた別コマンドの応答、または復帰確認コマンドのNACKとして切り分ける |
| timeout | リスタート送信直後なら正常系。復帰確認コマンドで発生した場合は未復帰または接続問題 |
| ACKらしき `CMD=30h` | 本コマンドの成功ACKとは扱わない。別コマンド応答・バッファ残留・再同期対象として確認する |

### 8.4 AI実装用レスポンス定義

#### 共通フレームoffset

| offset | フィールド | 実装上の意味 |
|---:|---|---|
| 0 | `STX` | 常に `02h`。異なる場合は `INVALID_FRAME` |
| 1 | `ADR` | 通常はリーダライタID。RFタグ応答でアンテナID出力ONの場合は読み取りANT番号 |
| 2 | `CMD` | 復帰確認コマンドでは `30h`=ACK、`31h`=NACK等。本リスタート自体のACK/NACKではない |
| 3 | `LEN` | `DATA`部のbyte数。総フレーム長は `LEN + 7` |
| 4..`4+LEN-1` | `DATA` | 復帰確認コマンド側の定義で読む |
| `4+LEN` | `ETX` | 常に `03h`。異なる場合は `INVALID_FRAME` |
| `5+LEN` | `SUM` | `STX`から`ETX`までのSUM下位1byte |
| `6+LEN` | `CR` | 常に `0Dh` |

#### 最小疑似コード

```text
before = read_startup_snapshot_if_needed()
send_restart_frame("02 00 4E 01 9D 03 F1 0D")
# ACK/NACKは待たない。レスポンスなしが仕様。
sleep_at_least(2.0 seconds)
reopen_port_if_needed()
rom = read_rom_version(timeout)
if rom.ok:
    after = read_startup_snapshot_if_needed()
    return RESTART_CONFIRMED(before, after)
return RESTART_CONFIRM_TIMEOUT
```

#### 推奨パーサ出力

```json
{
  "frame_type": "NO_RESPONSE_EXPECTED | RESTART_CONFIRMED | RESTART_CONFIRM_TIMEOUT | SEND_FAILED | INVALID_FRAME_DURING_RESTART | POST_RESTART_NACK",
  "command": "リスタート",
  "command_bytes": "4E 9D",
  "tx_hex": "02 00 4E 01 9D 03 F1 0D",
  "ack_expected": false,
  "nack_expected": false,
  "restart_wait_seconds_min": 2.0,
  "post_restart_probe": "ROMバージョン読み取りなど低影響コマンド",
  "ram_settings_reset_to_flash": true,
  "settings_snapshot_used": true,
  "is_success": false,
  "error": null,
  "raw_hex_policy": "PDF掲載例は可。実機ログ由来のEPC/UII/TID/パスワードはマスク"
}
```

#### 設定スナップショット必須項目

実行前後に、ROM/機種、物理アンテナ容量、接続OKアンテナ、現在ANT、アンテナID出力、TID付加、EPC/UII応答設定、読取完了応答、アンテナ切替完了応答、キャリア検知応答、RAM設定、FLASH由来設定への復帰有無を確認してください。

## 9. 実機確認

実機確認区分: `needs-metadata-confirmation`

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

