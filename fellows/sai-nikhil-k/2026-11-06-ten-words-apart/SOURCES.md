# SOURCES — Ten Words Apart

## Provenance

Sai gave the topic and URL (2026-11-09) as the second video for the week of
11-06, asked for many images and light math, and chose the angle and title.

## Sources

| What | Where | Used for |
|---|---|---|
| Sasha Savsunenko, "Inducing creativity in LLM models", Nov 5, 2026 | https://crazylog.substack.com/p/inducing-creativity-in-llm-models · repo copy `research/savsunenko_post_f4715f6.md` | the experiment and the author's framing |
| The author's repo (MIT) | https://github.com/crazyleg/dat-grpo-creativity @ `f4715f6` · `research/dat_grpo_README_f4715f6.md`, `research/noun-verb-full250-dat-results-2026-11-03.md`, `research/sol-table_f4715f6.md`, `research/capabilities-table_f4715f6.md` | raw word lists (re-scored), judge and IFEval numbers, figures |
| Model card | https://huggingface.co/crazyleg11/qwen3.8-27b-dat-grpo-full250 | 27B, 250 GRPO updates, open weights (screenshot) |
| The DAT | Olson et al., "Naming unrelated words predicts creativity", PNAS 118(25) e2022340118 (2021); code https://github.com/jayolson/divergent-association-task @ `9978dd8` (MIT) · `research/divergent_association_task_README_9978dd8.md` | the score and its formula |
| GloVe 840B 300d | Stanford NLP, via https://huggingface.co/stanfordnlp/glove (zip sha256 f47355dd5b26…) | the word vectors the scorer uses |
| WordNet 3.0 | via nltk 3.10.4 | the adjective check |

## Images

| File | What | Credit / licence |
|---|---|---|
| `hf_full250.png` | model card screenshot | the author's card (weights Apache-2.0) |
| `fig_creative_transfer.png`, `fig_poems.png`, `fig_dat_validity.png` | the author's figures | Sasha Savsunenko, MIT |
| `list_farm*.png`, `list_far*.png`, `adj_tiles.png` | word-tile composites (make_tiles.py) | composites of the photos below |

Word photos (Wikimedia Commons):

| File | Word | Author | Licence | Page |
|---|---|---|---|---|
| `w_bark.jpg` | bark | Gregory Schick aka leadgolem | Public domain | https://commons.wikimedia.org/wiki/File:Bark_cortex_texture.jpg |
| `w_cat.jpg` | cat | Dmitry Makeev | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Black_cat_portraits.jpg |
| `w_contour.jpg` | contour | National Centers for Environmental Prediction | Public domain | https://commons.wikimedia.org/wiki/File:2005-10-29_500-Millibar_Height_Contour_Map_NOAA.png |
| `w_cow.jpg` | cow | Dietrich Michael Weidmann | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:2011-11-30-Mezlando_(Foto_Dietrich_Michael_Weidmann)_243.JPG |
| `w_crumb.jpg` | crumb | Safa.daneshvar | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:011221-ATN-IMG_4005.jpg |
| `w_dog.jpg` | dog | Muldoonsamuel | CC0 | https://commons.wikimedia.org/wiki/File:A_Labrador_Retriever_in_Aurora,_Colorado.jpg |
| `w_gavel.jpg` | gavel | perpetual.fostering | CC BY 2.0 | https://commons.wikimedia.org/wiki/File:Adoption_applications_forms_on_wooden_surface_with_gavel._-_51001450775.jpg |
| `w_glacier.jpg` | glacier | Valentinamaur | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Glaciar_Perito_Moreno,_Argentina,_enero_2024.jpg |
| `w_goat.jpg` | goat | Béria Lima de Rodríguez | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:Baby_Goat_in_Margarita_Island,_Venezuela.jpg |
| `w_horse.jpg` | horse | Jules Verne Times Two | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Bay_horse_grazing,_Fenais_da_Luz,_S%C3%A3o_Miguel_Island,_Azores,_Portugal_(PPL1-Corrected)-2.jpg |
| `w_justice.jpg` | justice | DP Singh Bhullar | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Close-up_of_Lady_Justice_statue_holding_scales,_symbolizing_justice_and_fairness.jpg |
| `w_mule.jpg` | mule | Unknown authorUnknown author | Public domain | https://commons.wikimedia.org/wiki/File:Catharine_mule_arabe_issue_de_Barbe.jpg |
| `w_pig.jpg` | pig | Gzen92 | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Cochon_domestique_(Sus_scrofa_domesticus)_(2).jpg |
| `w_receipt.jpg` | receipt | Bernd Schwabe | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:2023-10-20_Ausstellung_%22The_Mystery_of_Banksy_-_A_genius_Mind%22_im_Aufhof_in_Hannover,_Rechnung_Cofo_Entertainment_GmbH_%26_Co._KG_in_Passau,_Plastiktasche.jpg |
| `w_sheep.jpg` | sheep | Rude Health | CC BY-SA 2.0 | https://commons.wikimedia.org/wiki/File:Sheep_Pasture_-_geograph.org.uk_-_3568613.jpg |
| `w_spoon.jpg` | spoon | Silar | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:02021_0126-001_Table_centrepiece_silverware;_spoon,_tureen_ladle,_fork,_salad_spoon,_Krak%C3%B3w,_before_1915,_M._Jarra.jpg |
| `w_staple.jpg` | staple | Jacek Halicki | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:2023_Zszywki.jpg |
| `w_suture.jpg` | suture | Saltanat ebli | CC0 | https://commons.wikimedia.org/wiki/File:CHROMIC_(sterilized_surgical_suture).2_USP.37mm_01.JPG |
| `w_tiger.jpg` | tiger | Luis Miguel Bugallo Sánchez (Lmbuga) | CC BY-SA 3.0 | https://commons.wikimedia.org/wiki/File:08-2011._Panthera_tigris_tigris_-_Texas_Park_-_Lanzarote_-TP00.jpg |
| `w_violin.jpg` | violin | David Schou | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:Baroque_violin_Walter_Mahr,_2010_-_Violin_Joseph_Chevrier,_1889.jpg |
| `w_volcano.jpg` | volcano | Giles Laurent | CC BY-SA 4.0 | https://commons.wikimedia.org/wiki/File:001_Volcano_eruption_of_Litli-Hr%C3%BAtur_in_Iceland_in_2023_Photo_by_Giles_Laurent.jpg |

Every file has a sidecar `images/src/<slug>.json`.

## Honesty log

- **The post's text says less than its repo.** The post reports clear creativity
  and imagery gains; the repo also reports lower coherence and the adjective
  collapse. The reel follows the repo.
- **Re-scored, not quoted:** every DAT mean on screen comes from our run of the
  official scorer on his raw lists; the adjective check is our own WordNet run.
- **Quoted, the author's:** the AI-judge table, the writing benchmarks and IFEval.
- **Our two lists are illustrations**, not data from the experiment.
- **Photo picks:** seven automatic Commons picks were replaced after review
  (wrong subject, or a graphic surgery photo).
