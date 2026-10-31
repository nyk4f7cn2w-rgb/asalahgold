# asalahgold
Official website of ASALAH GOLD — https://asalahgold.com

موقع ثابت (HTML واحد) يُنشر عبر GitHub Pages من الفرع `main`.

## بنية المشروع
| المسار | الوصف |
|---|---|
| `index.html` | الصفحة الرئيسية (الأنميشن، القاعات، المعرض، التواصل) |
| `gallery/` | الصور الأصلية للمجوهرات — لا تُعدَّل ولا تُحذف |
| `gallery/opt/` | نسخ WebP خفيفة تُولَّد تلقائياً من الأصلية (640 و1600 بكسل) |
| `gallery/catalog.json` | قائمة القطع: الرقم، الصنف، "أحدث الإضافات" |
| `assets/` | أيقونات الموقع وصورة المشاركة (og-image) |
| `version.json` | رقم الإصدار — يُستخدم لإجبار المتصفح على تحميل آخر نسخة |
| `tools/` | سكربتات الصيانة |

## إضافة صورة جديدة
1. ارفع الصورة إلى `gallery/`.
2. أضف سطراً لها في `gallery/catalog.json` (الصنف أحد: `necklaces`, `sets`, `bangles`, `bullion`, `showroom`).
3. شغّل:
   ```
   python3 tools/optimize_images.py
   python3 tools/build_gallery.py
   sh tools/stamp_version.sh
   ```
4. ارفع التغييرات (commit + push).

## قبل كل نشر
شغّل `sh tools/stamp_version.sh` حتى يتغيّر رقم الإصدار؛ أي زائر عنده نسخة قديمة مخزّنة يُحدَّث تلقائياً مرة واحدة.

## صفحات قديمة
`preview.html` و`animation-preview.html` و`gallery.html` باقية كما هي لكنها مستبعدة من محركات البحث (`noindex`) وتشير إلى الصفحة الرئيسية.
