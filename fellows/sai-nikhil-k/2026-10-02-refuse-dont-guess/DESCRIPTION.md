Gavia now checks 25 photos at once. Pick 26 and it checks none — on purpose.

This weekly progress reel opens Gavia 0.3.0 and 0.3.1, a free, offline desktop app that finds common loons in field photographs. Last week's plan was survey counting: a whole folder, one total, one CSV. This week got part of the way. You can now pick up to 25 photos, or a zip of them, and Gavia checks them one at a time with a progress bar and a Stop button.

We ran it in the real app on 25 freely licensed photos: 22 with loons and 3 empty lakes. On an M2 Pro laptop all 25 took about three and a half seconds. The app counted loons in 23 of 25. The truth is 22: one empty lake came back with a box drawn on a pine branch, at 41% confidence. The count is where review starts, not where it ends.

The design question this release had to answer: what happens to the photo that doesn't fit? The easy fix is to check the first 25 and quietly drop one. But which one was dropped would be a guess, and a survey with a silent hole in it looks exactly like a complete one. So Gavia refuses the whole selection and says how many it counted: "That's 26 images. You can check up to 25 at a time." Images inside zips count too. The zip limit comes from the same numbers: 25 images × 20 MiB = 500 MiB, so a zip bigger than any legal batch is turned away before it is opened.

A file it can't read is a different case. A notes.txt inside a zip, or a photo over 20 MiB, is left out and named, and everything else goes through. We ran Gavia's own selection code on this video's photos: 25 photos → 25 checked; 26 → 0; a zip of 25 plus one loose photo → 0; 24 photos plus one oversized file → 24, with the oversized one named.

The other change is updates, in 0.3.0. When Gavia starts, it asks GitHub for a small file (1,833 bytes) naming the newest release. If that release is newer, Gavia downloads it in the background, checks its signature and offers a restart. It never restarts by itself. We watched the app's network sockets during this video's run. There was one, to GitHub, at launch, and none while the photos were checked. One switch in Settings → Updates turns even that off.

What did not ship yet: checking a whole folder in one go, a single total of loons rather than a count of photos with loons, and a CSV export. Those are next on the roadmap.

Try it yourself: if something you are building has a limit, walk through the limit plus one before you ship it. If the answer is that something gets quietly dropped, ask who would notice, and when. A refusal costs your user one more click. A silent drop costs them an answer that is wrong and looks right.

Gavia, the project in this reel: https://github.com/nikhil-kunapareddy/gavia

Chapters:
0:00 What happens to the 26th photo?
0:16 In the app: 25 photos, 3.5 seconds, 23 of 25
0:35 Trim to 25, or refuse all 26?
0:53 The rule, from the source: n · [n ≤ 25]
1:12 Gavia's own code, run on these photos
1:33 The one call home — and its off switch
1:53 Against last week's plan
2:09 Verdict — refuse, don't guess
2:25 Your turn: the limit plus one
2:40 Outro

Photographs (Wikimedia Commons; renamed photo-01 … photo-26 so the file name never gives away what is in the picture):
photo-01.jpg — “Common Loon (Gavia immer) (16332756641)” — Andrew C, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Common_Loon_(Gavia_immer)_(16332756641).jpg
photo-02.jpg — “Common Loon (Gavia immer) in the Morro Bay” — Mike Baird from Morro Bay, USA, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Common_Loon_(Gavia_immer)_in_the_Morro_Bay.jpg
photo-03.jpg — “Common Loon - Gavia immer, Delaware Seashore State Park, Rehoboth Beach, Delaware (24937761707)” — Judy Gallagher, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Common_Loon_-_Gavia_immer,_Delaware_Seashore_State_Park,_Rehoboth_Beach,_Delaware_(24937761707).jpg
photo-04.jpg — “Shoreline - Fanshawe Lake (20907396514)” — WabbitWanderer from London, Canada, CC BY-SA 2.0 (https://creativecommons.org/licenses/by-sa/2.0) — https://commons.wikimedia.org/wiki/File:Shoreline_-_Fanshawe_Lake_(20907396514).jpg
photo-05.jpg — “Common Loon - Gavia immer, Ocean City Inlet, Ocean City, Maryland” — Judy Gallagher, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Common_Loon_-_Gavia_immer,_Ocean_City_Inlet,_Ocean_City,_Maryland.jpg
photo-06.jpg — “Common Loon - Gavia immer (20902253322)” — GlacierNPS, Public domain — https://commons.wikimedia.org/wiki/File:Common_Loon_-_Gavia_immer_(20902253322).jpg
photo-07.jpg — “Common Loon head sideways” — Art Weber/U.S. Fish and Wildlife Service, Public domain — https://commons.wikimedia.org/wiki/File:Common_Loon_head_sideways.jpg
photo-08.jpg — “Common Loon in Flight - Gavia immer (27909754751)” — GlacierNPS, Public domain — https://commons.wikimedia.org/wiki/File:Common_Loon_in_Flight_-_Gavia_immer_(27909754751).jpg
photo-09.jpg — “Common Loons (2) - Gavia immer (27909375811)” — GlacierNPS, Public domain — https://commons.wikimedia.org/wiki/File:Common_Loons_(2)_-_Gavia_immer_(27909375811).jpg
photo-10.jpg — “Common Loons - Gavia immer (27909381701)” — GlacierNPS, Public domain — https://commons.wikimedia.org/wiki/File:Common_Loons_-_Gavia_immer_(27909381701).jpg
photo-11.jpg — “Common loon (Gavia immer) on Meadow Lake (8201473748)” — Forest Service Northern Region from Missoula, MT, USA, Public domain — https://commons.wikimedia.org/wiki/File:Common_loon_(Gavia_immer)_on_Meadow_Lake_(8201473748).jpg
photo-12.jpg — “Boundary Waters Korb River” — Geoffrie, Public domain — https://commons.wikimedia.org/wiki/File:Boundary_Waters_Korb_River.JPG
photo-13.jpg — “Common loon (Gavia immer) on Meadow Lake (8201474062)” — Forest Service Northern Region from Missoula, MT, USA, Public domain — https://commons.wikimedia.org/wiki/File:Common_loon_(Gavia_immer)_on_Meadow_Lake_(8201474062).jpg
photo-14.jpg — “Common loon - Gavia immer” — lwolfartist, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Common_loon_-_Gavia_immer.jpg
photo-15.jpg — “Common loons swimming in Swan Lake (DSCF3780)” — Trougnouf, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0) — https://commons.wikimedia.org/wiki/File:Common_loons_swimming_in_Swan_Lake_(DSCF3780).jpg
photo-16.jpg — “Eistaucher (Gavia immer)” — Jens Freitag, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0) — https://commons.wikimedia.org/wiki/File:Eistaucher_(Gavia_immer).jpg
photo-17.jpg — “Gavia Immer CommonLoon LkCoochiching” — Mykola Swarnyk, CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0) — https://commons.wikimedia.org/wiki/File:Gavia_Immer_CommonLoon_LkCoochiching.jpg
photo-18.jpg — “Gavia immer1 BS” — Cephas, CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer1_BS.jpg
photo-19.jpg — “Little Gabro Lake, clouds, approaching sunset 765” — Dankarl, CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0) — https://commons.wikimedia.org/wiki/File:Little_Gabro_Lake,_clouds,_approaching_sunset_765.jpg
photo-20.jpg — “Gavia immer (30862067283)” — Melissa McMasters from Memphis, TN, United States, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_(30862067283).jpg
photo-21.jpg — “Gavia immer (31299418360)” — Melissa McMasters from Memphis, TN, United States, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_(31299418360).jpg
photo-22.jpg — “Gavia immer (Common Loon) 1APR2017” — ADJ82, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_(Common_Loon)_1APR2017.jpg
photo-23.jpg — “Gavia immer -Minocqua, Wisconsin, USA -swimming-8” — John Picken from Chicago, USA, CC BY 2.0 (https://creativecommons.org/licenses/by/2.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_-Minocqua,_Wisconsin,_USA_-swimming-8.jpg
photo-24.jpg — “Gavia immer Common loon 4827” — ImagePerson, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_Common_loon_4827.jpg
photo-25.jpg — “Gavia immer Common loon 4843” — ImagePerson, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_Common_loon_4843.jpg
photo-26.jpg — “Gavia immer Common loon 4910” — ImagePerson, CC BY 4.0 (https://creativecommons.org/licenses/by/4.0) — https://commons.wikimedia.org/wiki/File:Gavia_immer_Common_loon_4910.jpg [the 26th photo, used only in the code test]

Hosted by Sai. Voice: Kokoro am_onyx, free and local, no account. AI-generated narration. Motion graphics built with Remotion. The equations are typeset locally as outlined SVG. The two app sequences are screen recordings of the released Gavia 0.3.1 on a Mac, run against a scratch storage folder. They are shown in real time: the file dialog and one scroll are cut, and the scratch folder's path is covered. Every number on screen was re-measured for this video. The project's own tests were run at the release commit (257 interface tests and 115 Rust tests, all passing). Gavia's batch-selection code was run unmodified on these photos. Release sizes, update manifests and CI results come from GitHub's API. The README's "43 MB" download is not repeated, because the 0.3.1 DMG measures 46.1 MiB. No adoption or download figures appear, and no speed claim beyond this one run on this laptop. No image was generated. No human-performed audio or video in this production.

Gavia: https://github.com/nikhil-kunapareddy/gavia
Humanitarians AI: https://humanitarians.ai
Musinique: https://musinique.com
Medhavy AI: https://medhavy.com

TAGS: Gavia, loon detection, common loon, batch processing, zip files, input validation, limits, fail loudly, silent failure, Tauri, Rust, React, auto update, Tauri updater, desktop app, open source, conservation, Humanitarians AI, weekly progress, Computational Skepticism

#AI #ComputerVision #OpenSource #Conservation #SoftwareDesign #Rust #Tauri #HumanitariansAI #WeeklyUpdate
