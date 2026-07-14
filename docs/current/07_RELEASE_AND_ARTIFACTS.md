# Release And Artifacts

この文書では、UTR-S201 AI補助パッケージのReleaseとArtifactsを整理します。

## 1. 最新Release

最新Releaseは v022 Final RC です。

- Release tag: `utr-s201-ai-v022-final-rc.1`
- ZIP: `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip`
- SHA256: `2A7E97DE4A19B634EC49953B5E6815C307C90D0E420AA381E3AF5752C9166984`
- Release種別: pre-release
- PDF同梱: なし

## 2. v022 Final RCの位置づけ

v022は、現在のno-PDF UTR-S201 AI assistant packageをFinal RCとして統合した成果物です。

含むもの:

- v019 Stage 2 read completion
- v020 Stage 3+ high-impact readiness
- v021 Stage 3+ first batch planning
- AI context / frontmatter metadata
- 54 command cards
- current verification and HOLD notes

含まないもの:

- PDFファイル
- runtime logs
- 実CSVログ
- 顧客情報
- 実IPアドレス
- raw EPC / UII / TID
- 旧ZIP

## 3. 成果物履歴

| Version | ZIP / 文書 | 状態 |
|---|---|---|
| v008 | `artifacts/utr_s201_ai_v008/utr_s201_ai_v008_v117_full_coverage_no_pdf.zip` | full coverage package |
| v009 | `artifacts/utr_s201_ai_v009/utr_s201_ai_v009_v117_traceability_completed_no_pdf.zip` | traceability completed |
| v010 | `artifacts/utr_s201_ai_v010/utr_s201_ai_v010_real_device_verification_framework_no_pdf.zip` | real-device verification framework |
| v011 | `artifacts/utr_s201_ai_v011/utr_s201_ai_v011_stage01_readonly_verification_kit_no_pdf.zip` | Stage 0/1 read-only kit |
| v012 | `artifacts/utr_s201_ai_v012/utr_s201_ai_v012_stage0_readonly_real_device_result_no_pdf.zip` | Stage 0 result |
| v013 | `artifacts/utr_s201_ai_v013/utr_s201_ai_v013_stage0_rom_read_frame_adapter_no_pdf.zip` | ROM read adapter |
| v014 | `artifacts/utr_s201_ai_v014/utr_s201_ai_v014_stage0_remaining_readonly_result_no_pdf.zip` | Stage 0 remaining result |
| v015 | `artifacts/utr_s201_ai_v015/utr_s201_ai_v015_stage1_readonly_configuration_result_no_pdf.zip` | Stage 1 result |
| v016 | `artifacts/utr_s201_ai_v016/utr_s201_ai_v016_stage2_rf_read_preflight_no_pdf.zip` | Stage 2 preflight |
| v019 | `artifacts/utr_s201_ai_v019/utr_s201_ai_v019_stage2_read_completion_no_pdf.zip` | Stage 2 read completion |
| v022 | `artifacts/utr_s201_ai_v022/utr_s201_ai_v022_final_rc_no_pdf.zip` | Final RC |

v017、v018、v020、v021は、ZIP / GitHub Releaseを作成していません。

## 4. Release判断

GitHub成果物としては、v022 Final RC pre-releaseまで完了しています。

ただし、以下は別判断です。

- 正式社外公開承認
- 顧客提供判断
- ライセンス / IP最終確認
- 海外利用 / 海外販売判断
- Stage 3+ real-device execution
- 全54コマンドの個別実機送信確認

## 5. 安全上の注記

v022 package作成時点では、以下を実行していません。

- 実機送信
- 書き込み系コマンド送信
- FLASH write / init
- 周波数変更
- 送信出力変更
- アンテナ設定変更
- タグメモリ書き込み
- Lock / Kill / Encode / ThroughCmd送信
