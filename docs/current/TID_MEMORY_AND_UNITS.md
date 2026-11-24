# TIDメモリと長さの単位

確認日: 2026-09-07。メーカーSDKを前提とせず、規格の単位とUTR固有の読取り機能を分けて参照します。

## 1. 一次情報の役割

| 資料 | この文書で参照する範囲 |
|---|---|
| [GS1 Japan EPC/RFID標準](https://www.gs1jp.org/standard/epc/epcrfidstandards.html) | Gen2、TDS、メモリバンクの位置づけ |
| [GS1 Gen2 Release 3.0.1](https://ref.gs1.org/standards/gen2/3.0.1/) | §6.3.2.1 p.56のメモリ構成、§6.3.2.1.3 p.65のTID、§6.3.2.12.3.4 p.114の16-bit word定義 |
| [UTR-S201プロトコル Ver.1.17](https://www.product.takaya.co.jp/dcms_media/other/TDR-MNL-PRC-UTR-S201-117.pdf) | §3.9 p.59–60、§7.2 p.117–119、§7.5.2 p.266–270の製品固有の読取り・応答 |

Gen2規格の参照版を示すことは、UTRの全機種・ROMがその版の全機能へ対応しているという意味ではありません。UTRのコマンドや応答は対象機種のタカヤPDFで確認します。

## 2. Word・byte・bitの換算

Gen2のメモリ操作で扱う1 Wordは16 bitです。ここでは1 byte＝8 bitとして換算します。

| Word数 | byte数 | bit数 |
|---:|---:|---:|
| 1 | 2 | 16 |
| 4 | 8 | 64 |
| 6 | 12 | 96 |
| 8 | 16 | 128 |

この表は単位換算です。TID全体の長さを一律に64 bitや96 bitと規定する表ではありません。タグが実装するTIDの構成・長さ、UTRが要求する読取り範囲、応答の実際のbyte数を別々に確認します。

## 3. UTRのTID付加と原典の不整合

UTR-S201 PDF §3.9は、TID付加機能で6 Wordまたは4 Wordを読み取る処理と、6 Wordを超えるTIDの全体を付加できない制限を説明しています。これは製品機能の制限です。Gen2のTID一般の最大長ではありません。

同PDF p.267および[InventoryReadカード](commands/cards/55_14_uhf_inventory_read.md)の原典転記には、「4 Word＝96 bit、6 Word＝128 bit」という換算が残っています。GS1の16-bit word定義による正しい換算は **4 Word＝64 bit、6 Word＝96 bit** です。

原典の記録と区別するため、転記本文は保持し、RAGの解説としてこの訂正を付けます。タカヤによる正式な正誤表発行を意味しません。PDF画像での当該表記の確認は未完了ですが、単位換算の根拠はGS1公式規格で確認済みです。

## 4. AIが混同しないための確認

- TIDとEPC/UIIを同じ識別子として扱わない。
- UTRのTID付加機能と、任意範囲のタグメモリ読取りを分ける。
- Wordアドレス、Word数、応答中のbyte数を、それぞれのフィールド定義で確認する。
- TID付加設定の適用先は[モード別適用範囲](RESPONSE_MODE_APPLICABILITY.md)で確認する。
- 読み取ったTIDの一部分だけで個体識別が保証されるとは断定しない。対象タグの構成と取得範囲を確認する。
