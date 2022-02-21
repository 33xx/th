from userbot.Config import Config
from userbot.plugins import mention

RAZAN = Config.TG_BOT_USERNAME

ROZ = (
    f"**♰︙بوت ريـك يعمل بنجاح ♰،**\n"
    f"— — — — — — — — — — — — — —\n"
    f"**   - اصدار التليثون :♰ `1.23.0\n`"
    f"**   - اصدار ريـك :♰ `4.0.0`\n"
    f"**   - البوت المستخدم :** `{RAZAN}`\n"
    f"**   - اصدار البايثون :♰ `3.9.6\n`"
    f"**   - المستخدم :♰ {mention}\n"
    f"— — — — — — — — — — — — — —\n"
    f"Developers: @HvvHH \n"
)
# for alive command
ROZBOT = "**•❒ اوامـر البـوت**\n\n( `.السورس ` ) \n• لعرض معلومات السورس\n\n(  `.فحص`  ) \n• لعرض معلومات تنصيبك\n\nٴ╼──────────────────╾\n\n( `.تنصيب`  ) \n• بالرد على ملف لتنصيبه للسورس\n\n( `.الغاء التنصب < اسم الملف>`  ) \n• لالغاء تنصيب ملف من السورس اكتب الامر مع اسم الملف  -  بدون وضع  < >\n\nٴ╼──────────────────╾\n\n( `.تحديث الان`  )\n• لتحديث ملفات السورس اذا نزل تحديث من المطورين\n\n( `.اعادة تشغيل` ) \n• لاعادة تشغيل البوت اذا كان هناك مشكله في البوت استخدم الامر\n\nٴ╼──────────────────╾ \n\n( `.فاراتي`  ) \n• لعرض معلومات تنصيبك من ايبي هاي وكود تيرمكس  لا تستخدم الامر في المجموعات ولا تشارك معلوماتك\n\nٴ╼──────────────────╾\n\n( `.متى`  ) \n• بالرد على الرسالة لمعرفة تاريخ ارسالها و وقت ارسالها\n\nٴ╼──────────────────╾ \n\n( `.الملفات`  ) \n• لعرض جميع اسماء ملفات السورس\n\nٴ╼──────────────────╾ \n@K4KK44  -  @ckcck"
ROZSEG = "**•❒ اوامـر تحـويل الصـيغ والجهـات**\n\n( `.تحويل صورة` ) \n• بالرد علة ملصق لتحويله صورة \n\n( `.تحويل ملصق` ) \n• بالرد على صورة لتحويلها الى ملصق\n\n( `.تحويل voice` )\n• بالرد على مقطع اغنية لتحويله على شكل بصمة صوتية\n\n( `.تحويل mp3` )\n• بالرد على البصمة الصوتية لتحويلها على شكل  مقطع mp3\n\n( `.تحويل متحركة` ) \n• بالرد على فيديو يحوله الى متحركة gif\n\nٴ╼──────────────────╾\n\n( `.ضيف +  رابط مجموعة` ) \n• تستخدم الامر بمجموعتك تكتب الامر ورابط المجموعة التريد تخمط منها لازم كروب عام\n\n( `.وجه` ) \n• ترد على صورة او كلام او اي شي بالامر وراح يرسله لجميع المجموعات \n\n( `.حول` ) \n• تكتب الامر مع النص وراح يرسله لجميع الاشخاص الموجودين بحسابك\n\nٴ╼──────────────────╾\n@K4KK44  - @ckcck"
ROZPRV = "•❒ اوامـر حمـاية الخـاص\n\n( `.الحماية` تشغيل/تعطيل ) \n• لتشغيل امر الحمايه او تعطيله في الـخاص \n\n( `.سماح` ) \n• بالرد على الشخص للسماح له بالتكلم في الخاص وعدم\n\n( `.رفض` ) \n• بالرد على الشخص لرفضه من الخاص \n\n( `.المسموح لهم` )\n• فقط ارسل الامر لاظهار الاشخاص المسموح لهم والمرفوضين\n\nٴ╼──────────────────╾\n\n( `.تلكراف ميديا` ) \n• بالرد على صورة لجلب رابط تلكراف للصورة لأستخدامه في الفارات\n\n( `.تلكراف نص` ) \n• بالرد على مقاله او نص بالامر لجلب رابط تلكراف للمقالة\n\nٴ╼──────────────────╾ \n\n( `.خاص <معرف><رسالة>` )\n• تكتب الامر مع معرف المستخدم مع الرسالة وارسالها في اي مكان وسيقوم بتوجيه الرسالة الى المستخدم"
ROZADM = "**•❒ اوامـر الادمن**\n\n( `.حظر` ) \n• تقوم بالرد على شخص او وضع معرفه مع الامر وسيحظره من المجموعة\n\n( `.الغاء حظر` )\n• بالرد على الشخص او كتابة معرفه مع الامر لالغاء حظره\n\nٴ╼──────────────────╾\n\n( `.كتم` ) \n• تقوم بالرد على شخص او وضع معرفه مع الامر وسيكتمه من المجموعة\n\n( `.الغاء كتم` )\n• بالرد على الشخص او كتابة معرفه مع الامر لالغاء كتمه\n\nٴ╼──────────────────╾\n\n( `.تثبيت` ) \n• تقوم بالرد على الرسالة مع الامر وستثبت في المجموعة\n\n( `.الغاء التثبيت` )\n• بالرد على الرسالة مع الامر لإلغاء تثبيتها\n\nٴ╼──────────────────╾\n\n( `.رفع مشرف` ) \n•  تقوم بالرد على الشخص مع الامر و سيرفع مشرفا في المجموعة\n\n( `.تك` )\n • بالرد على الشخص مع الامر لإنزاله من الاشراف في المجموعة\n\nٴ╼──────────────────╾ \n\n( `.ارفع` ) \n• لرفع المستخدم في جميع المجموعات مع كافة الصلاحيات مع لقب مخفي\n\n( `.نزل` ) \n• لتنزيل الشخص من رتبة الاشراف في جميع المجموعات\n\nٴ╼──────────────────╾\n\n( `.الاحداث` )\n• لعرض اخر رسائل محذوفة في المجموعه يجب ان تكون مشرف\n\nٴ╼──────────────────╾\n\n@K4KK44"
# ها نغل عود صاير عود خمطت ملف صرت مطور؟
JMTRD = "**•❒ اوامـر الترحيب والردود**\n\n( `.ترحيب + ترحيبك` ) \n• اكتب الامر مع ترحيب في المجموعه ليرحب بالاعضاء الجدد\n\n( `.حذف الترحيبات` ) \n• فقـط ارسل الامر في المجموعة لحذف الترحيبات\n\nٴ╼──────────────────╾\n\n( `.الترحيبات` ) \n• ارسل الامر في المجموعه لعرض ترحيبات المجموعة\n\n( `.الترحيب السابق ايقاف/تشغيل` )\n• لتعطيل اخر ترحيب وضعته في المجموعة او تشغيل\n\nٴ╼──────────────────╾\n\n( `.اضف رد + ردك` ) \n• لوضع رد معين في المجموعة اكتب الامر وردك\n\n( `.حذف الردود` ) \n• فقـط ارسل الامر في المجموعة لحذف الردود المضافة\n\nٴ╼──────────────────╾\n\n( `.الردود` ) \n• ارسل الامر في المجموعه لعرض ردود المجموعة\n\nٴ╼──────────────────╾\n@K4KK44"
JMGR1 = "**•❒ اوامـر المجموعه**\n\n( `.تفليش` ) \n• كتابة  الامـر فقط في المجموعه لحظر جميع الاعضاء\n\nٴ╼──────────────────╾\n\n( `.حذف المحظورين` ) \n• كتابة  الامـر في الكروب لالغاء حظر جميع الاعضاء \n\n( `.اطردني` ) \n• فقـط ارسل الامر في المجموعة لمغادرة المجموعه التي تم ارسال الامر فيها\n\nٴ╼──────────────────╾\n\n( `.المحذوفين` ) \n• لعرض الحسابات المحذوفة في مجمـوعة معيـنة ولحذفهم ارسل .المحذوفين اطردهم\n\n( `.الاعضاء` ) \n• فقـط ارسل الامر في المجموعة لعرض اعضاء المجموعة\n\nٴ╼──────────────────╾\n\n( `.المشرفين` ) \n• ارسل الامر في المجموعه لعرض حسابات المشرفين\n\n( `.البوتات` )\n• ارسل الامر في المجموعه لعرض البوتات\n\nٴ╼──────────────────╾\n@K4KK44"
JMAN = "**•❒  اوامـر التسـلية**\n\n`.غبي`  `.القنابل`  `.اتصل`   `.قتل`    `.طوبة`\n\n`.مربعات`   `.حلويات`     `.نار`     `.شحن`\n\n`.افكر`    `.متت`    `.ضايج`    `.ساعة`\n\n`.مح`    `.قلب`     `.جيم`     `.الارض`\n\n`.قمر`      `.اقمار`     `.قمور `    `.نجمه`\n\n`.مكعبات`   `.مطر `     `.تفريغ`      `.فليم`\n\n`.احبك`    `.طائره`        `.شرطه `\n\n`.النضام الشمسي`    `.قاتل`       `.عين`\n\n`.افكرر`      `.افعى`         `.رج`      `.مايكرو`\n\n`.فايروس`    `.قطار`      `.موسيقى `\n\n`.رسم`   `.تحميل`     `.مربع`       `.دائره`\n\n`.انيم`    `.بشره`      `.قرد`      `.يد`\n\n`.العد التنازلي`        `.قلوب`\n\nٴ╼──────────────────╾\n • حميع الاوامر تستخدم بالضغط على الامر راح ينسخ وحده وارسله فقط"
JROZT = "**•❒ اوامـر الحسـاب **\n\n( `.اسم وقتي` )\n• بكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها .\n\n( `.انهاء اسم وقتي` )\n• لانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\nٴ╼──────────────────╾\n\n( `.بايو وقتي` )\n• بكتابة الامر لاضافة بايو وقتي حسب منطقة التي وضعتها .\n• لوضع البايو الخاص بك ارسل ( `.فار بايو` ) \n\n( `.انهاء بايو وقتي` )\n• لانهاء البايو الوقتي و ارجاع البايو الطبيعي . \nٴ\n╼──────────────────╾\n\n(  `.الصورة الوقتية`  )\n• لعمل صورة حسابك الشخصية يظهر عليها وقت وتتغير كل دقيقه لمزيد معلومات عن هذا الامر ارسل  `.فار وقتية`\n\n(  `.انهاء الصورة الوقتية` )\n• لأيقاف امر الصورة الوقتية\nٴ\n╼──────────────────╾\n\n( `.وضع اسم <اسمك>`  )\n• لتغيير اسم الحساب الشخصي الخاص بك على التليجرام.،  اكتب الامر مع اسم الحساب\n\n(  `.وضع بايو <بايو>` )\n• لتغيير نبذة الحساب الشخصي الخاص بك على التليجرام، اكتب الامر مع البايو الخاص بك\n\n(  `.حذف صورة`  )\n• لحذف صور الحساب الخاصه بك  بكتابه الامر لحذف صورة\n\n( `.وضع صورة <بالرد>` )\n•لتغيير صورة الحساب الشخصي الخاص بك على التليجرام اكتب الامر  بالرد على الصورة \n\nٴ╼──────────────────╾\n@K4KK44"
TKPRZ = "**•❒ اوامـر التنظيف والتكرار**\n\n( `.كرر  <عدد التكرار> <بالرد>` )\n• يقوم بتكرار النصوص والوسائط بالرد على الرسالة او الصورة  بامر كرر مع عدد التكرار\n\n( `.تكرار الملصق <بالرد عل ملصق>` ) \n• بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها\n\n( `.مكرر  < وقت بالثواني><عدد><بالرد>` )\n• بالرد على نص او صورة او اي شي يقوم بالتكرار  مع وقت معين .\n\n( `.ضع تكرار <العدد>` )\n• لمنع التكرار بالمجموعة الخاصة بك بالعدد الذي وضعته للعودة للوضع الطبيعي ضع 999999.\n\n╼──────────────────╾\n\n( `.سبام < كلمـة >` )\n• يقوم بتفصيخ احرف الكلمه وارسالها جربه بنفسك\n\n( `.وسبام < كلـمة >`)\n• كتابة الامر مع نص معين يقوم بتفصيخ الجمله كلمه كلمه وارسالها\n\nٴ╼──────────────────╾\n\n( `.تنظيف + عدد الرسائل` )\n• يقوم بحذف الرسائل اكتب الامر وعدد معين من الرسائل سيقوم بحذفها \n\nٴ╼──────────────────╾\n\n( `.مسح  <بالرد على النص>` )\n• فقط اكتب الامر بالرد على الرسالة ليقوم بحذفها \n\n( `.حذف رسائلي` )\n• اكتب الامر في اي مكان وسيقوم بحذف جميع رسائلك في الدردشه حتى لو لم يكن لديك صلاحيات \n\nٴ╼──────────────────╾\n\n@K4KK44"
GRTSTI = "**•❒ اوامـر الملصقات و منـوع**\n\n( .ملصق )\n• بالرد على الملصق لأخذه و عمل حزمه خاصة بك و اضافته بها\n\n( .حزمة )\n• بالرد على الملصق لنسخ الحزمة كاملة بداخل حزمة ملصقاتك الخاصة\n\n(.معلومات_الملصق )\n• بالرد على الملصق لعرض معلومات الحزمة\n\nٴ╼──────────────────╾\n\n( .صور +  عدد الصور + نص )\n• للحصول على صور من متصفح كوكل بكتابة الامر وعدد الصور الحد 10 واسم النص\n\n( .موقع + المكان )\n• للحصول على مكان في الخريطه و ارساله لك\n\n( `.صورة` )\n• بالرد على الشخص للحصول على صورة حسابه الشخصية.\n\n( `.صورة كلها` )\n• للرد على الشخص للحصول على صور حسابه الشخصية كلها.\n\n( `.سرعة الانترنت` )\n• ارسل الامر لقياس سرعة الانترنت\n\n( `.حساب` )\nكتابة الامر مع معادلة رياضية و سيقوم بحلها و ارسالها لك\n\nٴ╼──────────────────╾\n@K4KK44"
HERP = "**•❒ اوامـر الأكسـترا**\n\n( `.جلب الصورة` ) \n• بالرد على صورة ذاتية التدمير لتحميلها وارسالها لك في الرسائل المحفوظة بسرية تامة\n\n(  .الرابط  ) \n• اكتب الامر في المجموعة لعرض رابط المجموعة يجب ان تكون مشرف\n\n(  `.معنى <الاسم>`  ) \n• لعرض معنى اسمك وارسال رسالة مع وصف للاسم\n\n(  `.قراءة < بالرد على ملف>`  ) \n• بالرد على ملف لعرض ما في داخل الملف ونسخه وارساله  لك\n\n(  `.حالتي` )\n• لعرض حاله حسابك اذا كان محظور او لا في التلي\n\n( `.ايميل وهمي` ) \n\n• لصنع ايميل وهمي وارساله لك\n\n(  `.حاسبة` ) \n• لعرض حاسبة علمية يجب ان تفعل وضع الانلاين\n\n( `.تاريخ` )\n• بالرد على الشخص او كتابة معرفه مع الامر لعرض سجل اسماء حسابه.\n\n( `.الوقت` )\n• لعرض الوقت الحالي على شكل ملصق\n\n( `.وقت` )\n• لعرض الوقت الحالي على شكل كتابة\n\n( `.مؤقت <الوقت> < النص> ` )\n• يقوم بإرسال رسالة مؤقتة و حذفها بعد وقت معين\n\n( `.كورونا < الدولة>` )\n• للحصول على احصائيات فايروس كورونا اكتب الامر مع اسم الدولة بالانكليزي\n\n( `.صلاة` < اسم محافظة> )\n• اكتب الامر مع اسم محافظتك باللغه الانكليزية للحصول على اوقات الصلاة\n\nٴ╼──────────────────╾\n@K4KK44"
CLORN = "**•❒ اوامـر التقليد والانتحال**\n\n( `.انتحال` ) \n• بالرد على الشخص لنسخ حسابه بالكامل من صورة واسم وبايو  \n\n( `.اعادة` ) \n• لارجاع الحساب الى وضعه الطبيعي لما كان سابقا\n\nٴ╼──────────────────╾\n\n( `.تقليد` ) \n• بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n( `.الغاء التقليد` ) \n• بالرد على الشخص لايقاف التقليد\n\n( `.المقلدهم` ) \n• لاظهـار قائمه الاشخاص الذي فعـلت عليهم امر التقليد ولمسحهم ارسل  ( `.مسح المقلدهم` ) \n\nٴ╼──────────────────╾\n\n( `.تاك` + معرف + نص ) \n\n• لعمل تاك لشخص في الكروب و وضع التاك في النص \n• مثـال | .تاك @K4KK44  ههلا \n\n( `.للكل + نص` ) \n• لعمل تاك للكل مع النص اكتب الامر مع النص وارسله فقط\n\n( `.ابلاغ` )\n• بالرد على الشخص لعمل ابلاغ لمشرفين المجموعة\n\nٴ╼──────────────────╾\n\n@K4KK44"
T7SHIZ = "•❒ اوامـر ممتعـة للترفيـه\n\n`.اوصف`        .هينه`      `.كت`    `.نزوج`\n\n`.طلاك`    `.رفع مطي`    `.رفع زوجي`\n\n`.رفع مرتي`      `.رفع تاج`   `.نسبة الانوثة`\n\n`.نسبة الغباء`    `.نسبة الحب`   `.رفع قرد`\n\n`.رفع جلب`     `.رفع بكلبي`\n\nٴ╼──────────────────╾\n\nجميع هذه الاوامر تستخدم بالرد على المستخدم"
ROZ_IC = "https://telegra.ph/file/4e950e66f1400d97a177e.jpg"
ROE = "**♰ هـذه هي قائمة اوامـر سـورس ريـك ♰**"
