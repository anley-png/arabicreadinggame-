# Placeholder audio for development ONLY. pip install edge-tts ; python tools/generate_audio.py [--force]
# edge-tts is unofficial: do NOT ship its output in a paid release. Replace audio/*.mp3 with recorded
# human voice (same filenames) or output from a service whose terms allow app use.
import asyncio, sys, pathlib, edge_tts
VOICE = "ar-SA-ZariyahNeural"
LET = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"          # same order as L in index.html -> l0..l27.mp3
WORDS = ["طالب","بيت","كتاب","باب","قمر","نبت","تبن","بحر","نهر","جمل","ولد","بنت","قلم","شمس","نجم","سمك","ورد","دب","كلب","ليل","نار","شجر","ثلج","حوت","فيل","تمر","عين","يد","سن","جبل","ديك","ابن","جد","فخذ","ذيل","رجل","زيت","خبز","نمر","دجاج","ضفدع","ظبي","غصن","فم","لبن","مطر","نحل","هرم","وجه","شاي","تفاح","ذباب","صوت","ضيف","غزال","قطار","كرسي","مفتاح","وقت","صحن","شباك","ضباب","طبيب","عصفور","ثعلب","دم","ورق","طباخ","دماغ","رياض","ميراث","رباط","ذراع","دف","جبال","ديوان","شاه","ناس","بنات","ملاك","حفاظ","حوض","قفص","صبح","نخل","وعد","نظر","حفظ","بيض","وضع","قصر","بطل","قطط","عشب","نسر","سكر","بحث","طبخ","سمع","صبغ","كهف","صيف","خيط","شفق","قلب","حليب","مثل","عيش","رش","رصاص","غضب","بغل","بقر","عنب","نور","فول"]  # same order as W -> w0.mp3, w1.mp3 ...
out = pathlib.Path("audio"); out.mkdir(exist_ok=True)
async def gen(text, name):
    p = out / name
    if p.exists() and "--force" not in sys.argv: return
    await edge_tts.Communicate(text, VOICE, rate="-25%").save(str(p))
async def main():
    for i, c in enumerate(LET): await gen(("أ" if i == 0 else c) + "َ", f"l{i}.mp3")
    for i, w in enumerate(WORDS): await gen(w, f"w{i}.mp3")
asyncio.run(main())
