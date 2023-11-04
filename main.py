def on_mob_killed_chicken():
    mobs.spawn(mobs.monster(GHAST), pos(0, 0, 0))
    mobs.spawn(mobs.monster(GHAST), pos(0, 0, 0))
    mobs.spawn(mobs.monster(GHAST), pos(0, 0, 0))
mobs.on_mob_killed(CHICKEN, on_mob_killed_chicken)

def on_mob_killed_sheep():
    mobs.spawn(mobs.monster(ZOMBIE), pos(0, 0, 0))
    mobs.spawn(mobs.monster(ZOMBIE), pos(0, 0, 0))
    mobs.spawn(mobs.monster(ZOMBIE), pos(0, 0, 0))
    gameplay.title(mobs.target(LOCAL_PLAYER),
        "§eAnimal dies = §mMob spawn",
        "made by EndBP on github")
mobs.on_mob_killed(SHEEP, on_mob_killed_sheep)

def on_mob_killed_villager():
    mobs.spawn(mobs.monster(VINDICATOR), pos(0, 0, 0))
    mobs.spawn(mobs.monster(VINDICATOR), pos(0, 0, 0))
    mobs.spawn(mobs.monster(VINDICATOR), pos(0, 0, 0))
mobs.on_mob_killed(VILLAGER, on_mob_killed_villager)

def on_mob_killed_cow():
    mobs.spawn(mobs.monster(WITCH), pos(0, 0, 0))
    mobs.spawn(mobs.monster(WITCH), pos(0, 0, 0))
    mobs.spawn(mobs.monster(WITCH), pos(0, 0, 0))
mobs.on_mob_killed(COW, on_mob_killed_cow)

def on_mob_killed_donkey():
    mobs.spawn(mobs.monster(ENDERMITE), pos(0, 0, 0))
    mobs.spawn(mobs.monster(ENDERMITE), pos(0, 0, 0))
    mobs.spawn(mobs.monster(ENDERMITE), pos(0, 0, 0))
mobs.on_mob_killed(DONKEY, on_mob_killed_donkey)

def on_mob_killed_wolf():
    mobs.spawn(mobs.monster(BLAZE), pos(0, 0, 0))
    mobs.spawn(mobs.monster(DROWNED), pos(0, 0, 0))
    mobs.spawn(mobs.monster(BLAZE), pos(0, 0, 0))
mobs.on_mob_killed(WOLF, on_mob_killed_wolf)

def on_mob_killed_pig():
    mobs.spawn(mobs.monster(SKELETON), pos(0, 0, 0))
    mobs.spawn(mobs.monster(SKELETON), pos(0, 0, 0))
    mobs.spawn(mobs.monster(SKELETON), pos(0, 0, 0))
mobs.on_mob_killed(PIG, on_mob_killed_pig)
