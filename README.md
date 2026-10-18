# Arabic Letter Island
Cartoon game that teaches non-Arabic speakers (kids and adults) to read Arabic letters and words.
Plain HTML/CSS/JS, no build step, works offline as a PWA.

## What is in this version
- Touch a letter: sound + name + slow-motion write reveal (28 letters)
- Forms room: isolated / initial / medial / final, shy letters locked, "shape-shift all"
- Words (7): Watch (0.5 s per letter, colours, shy-letter message), Build it (right-to-left boxes, kind wrong-answer feedback), Fix it
- Position Toss: pot / hens / mouse / house
- Island: every word built adds an emoji to your island; stars; 10-minute stretch-break toast; reduced-motion respected

## Run
`python3 -m http.server 8000` then open http://localhost:8000 (the service worker needs http, not file://).

## Put it on GitHub Pages
1. Create a repo, upload these files (keep the folder structure).
2. Settings > Pages > Deploy from branch > main / root.

## Audio
Browser TTS is the fallback. Better: put files in `audio/` named `l0..l27.mp3` (letters, order of `L`) and `w0..w6.mp3` (words, order of `W`).
`tools/generate_audio.py` makes placeholders with edge-tts. Do not ship those in a paid release: record a native speaker (signed release) instead.

## Add a letter/word
Edit `L` and `W` at the top of the script in index.html. `L` = [char, name, sound, joinsToNext]; `W` = [letter indexes, word, meaning, emoji]. Joining uses Unicode ZWJ, so the font does the shaping.

## Android / Play Store (Capacitor)
`npm init -y && npm i @capacitor/core @capacitor/cli @capacitor/android`, `npx cap init`, set webDir to this folder, `npx cap add android`, `npx cap sync`, open in Android Studio, build a signed AAB, upload in Play Console. Add the Billing plugin for a one-time unlock. If children are the audience, follow Google's Families policy. Add 192/512 icons of your own art.

## Roadmap (from the design notes)
Real SVG stroke paths + 4-form morph, characters in Rive, vowels (fatha/damma/kasra/sukoon), long vowels, deep vs soft sounds, mic practice, native-speaker review of every sound.

## Known limits
Writing animation is a reveal of the font glyph, not stroke-by-stroke. Test visually on a real phone, especially Arabic joining between coloured letters.

## v2 additions
Canvas tracing for any letter/form (coverage check, no stroke order yet), Sounds screen (short + long vowels), 31 words, animated SVG cat, connector-style forms, mistake tracking that makes Toss repeat weak letters ("Practice" on the Island). Vowel clips: `v<letter>_<0-6>.mp3`.

## Android app without Android Studio (GitHub builds it for you)
1. Edit `appId` in `capacitor.config.json` (for example `com.yourname.arabicletterisland`); it must be unique for the Play Store.
2. Push to `main`. Open Actions > "Build Android APK" > latest run > Artifacts > download `arabic-letter-island-apk`.
3. Unzip, copy `app-debug.apk` to your phone and install it (allow "install unknown apps").
4. For the Play Store you need a signed release AAB: create a keystore, store it as GitHub secrets, and change the last build step to `./gradlew bundleRelease` plus signing. Add the Play Billing plugin for a one-time unlock.
Note: recorded audio files are more reliable than browser TTS inside the Android WebView.
