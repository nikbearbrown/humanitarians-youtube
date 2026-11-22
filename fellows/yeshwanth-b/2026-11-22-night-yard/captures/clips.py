"""Exact take windows used by the GDD film, chosen by looking at the takes (contact sheets and the
input logs' state changes). Segments are (kind, first_frame, frame_count) in 30 fps video frames."""

FACTS = {
    'asserts': 78, 'asserts_words': 'seventy-eight',          # 39 + 22 + 17, all passing
    'boss_kos': 5, 'boss_kos_words': 'five times',            # level 6 "Times K.O.'d 5" (campaign frame 14800)
}

CLIPS = {
    # level 1: banner, a light (+10), a flying kick KO, the gate opening, the walk-through and Level Clear
    'core_loop': {'take': 'campaign', 'segments': [('play', 700, 70), ('play', 940, 60), ('play', 1180, 130),
                                                   ('play', 1600, 70), ('play', 1890, 140)]},
    # level 1 start: D held, Shift on and off (run / walk), Space onto the block
    'moves_run': {'take': 'campaign', 'segments': [('play', 785, 175)]},
    # level 2 shaft: wall slide 2734, wall jump 2735, grab 2746, climb 2754
    'shaft': {'take': 'campaign', 'segments': [('play', 2690, 120)]},
    # extras: jab, cross (800-810), uppercut 852, block 897-937, hammer 953
    'combo': {'take': 'extras', 'segments': [('play', 790, 230)]},
    # level 3: pickup 3984, throw 4002, the axe hits the bot
    'axe_throw': {'take': 'campaign', 'segments': [('play', 3960, 100)]},
    # defeat: checkpoint, step onto the plate, spikes 1645, K.O., respawn at the checkpoint
    'spikes': {'take': 'defeat', 'segments': [('play', 1560, 200)]},
    # level 6: a K.O. by the Forewoman (12654), then her last hit point and the gate (13950)
    'boss': {'take': 'campaign', 'segments': [('play', 12560, 140), ('play', 13880, 110)]},
    # character select: hover each Y Bot, click Yellow (609), Play (688)
    'select': {'take': 'campaign', 'segments': [('play', 430, 270)]},
    # defeat: Options (1974), Back (2093), Resume (2152), Esc -> panel over the running game (2234)
    'r01': {'take': 'defeat', 'segments': [('play', 1965, 300)]},
}
