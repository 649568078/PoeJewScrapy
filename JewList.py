class Jewlist:
    def together_mid(self):
        together_list = []
        name, test = self.ranshao_mid()
        together_list.append([name, test])
        name, test = self.hundun_mid()
        together_list.append([name, test])
        name, test = self.wuli_mid()
        together_list.append([name, test])
        name, test = self.bingleng_mid()
        together_list.append([name, test])
        name, test = self.chixu_mid()
        together_list.append([name, test])
        name, test = self.NonDamagingAilments_mid()
        together_list.append([name, test])
        name, test = self.affectedbyaHerald_mid()
        together_list.append([name, test])
        name, test = self.minionsaffectedbyaHerald_mid()
        together_list.append([name, test])
        name, test = self.ExertedAttacks_mid()
        together_list.append([name, test])
        name, test = self.CriticalStrikeChance_mid()
        together_list.append([name, test])
        name, test = self.MinionsmaximumLife_mid()
        together_list.append([name, test])
        name, test = self.AreaDamage_mid()
        together_list.append([name, test])
        name, test = self.ProjectileDamage_mid()
        together_list.append([name, test])
        name, test = self.TrapMine_mid()
        together_list.append([name, test])
        name, test = self.TotemDamage_mid()
        together_list.append([name, test])
        name, test = self.BrandDamage_mid()
        together_list.append([name, test])
        name, test = self.ChannellingSkills_mid()
        together_list.append([name, test])
        name, test = self.FlaskEffectDuration_mid()
        together_list.append([name, test])
        name, test = self.LifeRecoveryfromFlasks_mid()
        together_list.append([name, test])
        return together_list

    def ranshao_mid(self):
        Jew_name = '燃烧伤害中型'
        test = [['Eye of the Storm', 'pre'], ['Master of Fire', 'pre'],
                ['Smoking Remains', 'pre'], ['Cremator', 'pre'],
                ['Blowback', 'pre'], ['Fan the Flames', 'pre'],
                ['Cooked Alive', 'pre'], ['Burning Bright', 'pre'],
                ['Wrapped in Flame', 'pre'],
                ['Wasting Affliction', 'pre'], ['Haemorrhage', 'pre'],
                ['Flow of Life', 'pre'], ['Exposure Therapy', 'pre'],
                ['Brush with Death', 'pre'],
                ['Vile Reinvigoration', 'pre'],
                ['Circling Oblivion', 'pre'],
                ['Brewed for Potency', 'pre'],
                ['Student of Decay', 'pre'], ]
        return test, Jew_name

    def hundun_mid(self):
        Jew_name = '混沌持续中型'
        test = [['Unwaveringly Evil', 'pre'],
                ['Dark Ideation', 'pre'],
                ['Wicked Pall', 'pre'], ['Septic Spells', 'pre'],
                ['Low Tolerance', 'pre'], ['Steady Torment', 'pre'],
                ['Eternal Suffering', 'pre'],
                ['Eldritch Inspiration', 'pre'],
                ['Wasting Affliction', 'pre'], ['Haemorrhage', 'pre'],
                ['Flow of Life', 'pre'], ['Exposure Therapy', 'pre'],
                ['Brush with Death', 'pre'],
                ['Vile Reinvigoration', 'pre'],
                ['Circling Oblivion', 'pre'],
                ['Brewed for Potency', 'pre'],
                ['Student of Decay', 'pre'], ]
        return test, Jew_name

    def wuli_mid(self):
        Jew_name = '物理持续中型'
        test = [['Wound Aggravation', 'pre'], ['Vivid Hues', 'pre'],
                ['Rend', 'pre'], ['Disorienting Wounds', 'pre'],
                ['Compound Injury', 'pre'],
                ['Blood Artist', 'pre'], ['Phlebotomist', 'pre'],
                ['Steady Torment', 'pre'],
                ['Wasting Affliction', 'pre'], ['Haemorrhage', 'pre'],
                ['Flow of Life', 'pre'], ['Exposure Therapy', 'pre'],
                ['Brush with Death', 'pre'],
                ['Vile Reinvigoration', 'pre'],
                ['Circling Oblivion', 'pre'],
                ['Brewed for Potency', 'pre'],
                ['Student of Decay', 'pre'], ]
        return test, Jew_name

    def bingleng_mid(self):
        Jew_name = '冰冷持续中型'
        test = [['Cold-Blooded Killer', 'pre'],
                ['Wasting Affliction', 'pre'],
                ['Haemorrhage', 'pre'],
                ['Flow of Life', 'pre'],
                ['Exposure Therapy', 'pre'],
                ['Brush with Death', 'pre'],
                ['Vile Reinvigoration', 'pre'],
                ['Circling Oblivion', 'pre'],
                ['Brewed for Potency', 'pre'],
                ['Chilling Presence', 'pre'],
                ['Deep Chill', 'pre'],
                ['Blast-Freeze', 'pre'],
                ]
        return test, Jew_name

    def chixu_mid(self):
        Jew_name = '持续伤害中型'
        test = [['Wasting Affliction', 'pre'], ['Haemorrhage', 'pre'],
                ['Flow of Life', 'pre'], ['Exposure Therapy', 'pre'],
                ['Brush with Death', 'pre'],
                ['Vile Reinvigoration', 'pre'],
                ['Circling Oblivion', 'pre'],
                ['Brewed for Potency', 'pre'],
                ['Student of Decay', 'pre'], ]
        return test, Jew_name

    def NonDamagingAilments_mid(self):
        Jew_name = '非伤害中型'
        test = [['Eye of the Storm', 'pre'],
                ['Astonishing Affliction', 'pre'],
                ['Cold Conduction', 'pre'],
                ['Inspired Oppression', 'pre'],
                ['Chilling Presence', 'pre'],
                ['Deep Chill', 'pre'],
                ['Blast-Freeze', 'pre'],
                ['Stormrider', 'pre'],
                ['Overshock', 'pre'],
                ]
        return test, Jew_name

    def affectedbyaHerald_mid(self):
        Jew_name = '捷光环中型'
        test = [
            ['Self-Fulfilling Prophecy', 'pre'],
            ['Agent of Destruction', 'pre'],
            ['Dark Messenger', 'pre'],
            ['Empowered Envoy', 'pre'],
            ['Endbringer', 'pre'],
            ['Lasting Impression', 'pre'],
            ['Heraldry', 'pre'],
            ['Purposeful Harbinger', 'pre'],
        ]
        return test, Jew_name

    def minionsaffectedbyaHerald_mid(self):
        Jew_name = '召唤物捷光环中型'
        test = [
            ['Purposeful Harbinger', 'pre'],
            ['Heraldry', 'pre'],
            ['Endbringer', 'pre'],
            ['Cult-Leader', 'pre'],
            ['Lasting Impression', 'pre'],
            ['Invigorating Portents', 'pre'],
            ['Pure Agony', 'pre'],
            ['Disciples', 'pre'],
        ]
        return test, Jew_name

    def ExertedAttacks_mid(self):
        Jew_name = '增助攻击中型'
        test = [
            ['Lead By Example', 'pre'],
            ['Rattling Bellow', 'pre'],
            ['Cry Wolf', 'pre'],
            ['Mob Mentality', 'pre'],
            ['Provocateur', 'pre'],
            ['Warning Call', 'pre'],
            ['Haunting Shout', 'pre'],
        ]
        return test, Jew_name

    def CriticalStrikeChance_mid(self):
        Jew_name = '暴击几率中型'
        test = [['Precise Retaliation', 'pre'],
                ['Skullbreaker', 'pre'],
                ['Pressure Points', 'pre'],
                ['Overwhelming Malice', 'pre'],
                ['Magnifier', 'pre'],
                ['Savage Response', 'pre'],
                ['Eye of the Storm', 'pre'],
                ['Basics of Pain', 'pre'],
                ['Quick Getaway', 'pre'],
                ['Provocateur', 'pre'],
                ['Haemorrhage', 'pre'],
                ]
        return test, Jew_name

    def MinionsmaximumLife_mid(self):
        Jew_name = '召唤物生命中型'
        test = [['Renewal', 'pre'], ['Hulking Corpses', 'pre'],
                ['Dread March', 'pre'], ['Blessed Rebirth', 'pre'],
                ['Life from Death', 'pre'], ['Feasting Fiends', 'pre'],
                ['Bodyguards', 'pre']]
        return test, Jew_name

    def AreaDamage_mid(self):
        Jew_name = '范围伤害中型'
        test = [['Magnifier', 'pre'], ['Assert Dominance', 'pre'],
                ['Vast Power', 'pre'], ['Powerful Assault', 'pre'],
                ['Titanic Swings', 'pre'], ['Towering Threat', 'pre'],
                ['Expansive Might', 'pre'], ]
        return test, Jew_name

    def ProjectileDamage_mid(self):
        Jew_name = '投射物伤害中型'
        test = [['Repeater', 'pre'],
                ['Aerodynamics', 'pre'],
                ['Streamlined', 'pre'],
                ['Eye to Eye', 'pre'],
                ['Follow-Through', 'pre'],
                ['Shrieking Bolts', 'pre'],
                ]
        return test, Jew_name

    def TrapMine_mid(self):
        Jew_name = '地雷陷阱中型'
        test = [['Set and Forget', 'pre'],
                ['Expert Sabotage', 'pre'],
                ['Guerilla Tactics', 'pre'],
                ['Expendability', 'pre'],
                ['Arcane Pyrotechnics', 'pre'],
                ['Surprise Sabotage', 'pre'],
                ['Careful Handling', 'pre'],
                ]
        return test, Jew_name

    def TotemDamage_mid(self):
        Jew_name = '图腾伤害中型'
        test = [['Ancestral Echo', 'pre'], ['Ancestral Reach', 'pre'],
                ['Ancestral Might', 'pre'],
                ['Ancestral Preservation', 'pre'],
                ['Snaring Spirits', 'pre'],
                ['Sleepless Sentries', 'pre'],
                ['Ancestral Guidance', 'pre'],
                ['Ancestral Inspiration', 'pre'], ]
        return test, Jew_name

    def BrandDamage_mid(self):
        Jew_name = '烙印中型'
        test = [['Chip Away', 'pre'], ['Seeker Runes', 'pre'],
                ['Remarkable', 'pre'], ['Brand Loyalty', 'pre'],
                ['Holy Conquest', 'pre'], ['Grand Design', 'pre'], ]
        return test, Jew_name

    def ChannellingSkills_mid(self):
        Jew_name = '吟唱技能中型'
        test = [['Vital Focus', 'pre'],
                ['Rapid Infusion', 'pre'],
                ['Unwavering Focus', 'pre'],
                ['Enduring Focus', 'pre'],
                ['Precise Focus', 'pre'],
                ['Stoic Focus', 'pre'],
                ['Hex Breaker', 'pre']]
        return test, Jew_name

    def FlaskEffectDuration_mid(self):
        Jew_name = '药剂持续时间中型'
        test = [['Distilled Perfection', 'pre'],
                ['Spiked Concoction', 'pre'],
                ['Fasting', 'pre'], ["Mender's Wellspring", 'pre'],
                ['Special Reserve', 'pre'], ['Numbing Elixir', 'pre'],
                ['Brewed for Potency', 'pre'], ['Peak Vigour', 'pre'],
                ['Liquid Inspiration', 'pre'],
                ["Blizzard Caller", 'pre'], ]
        return test, Jew_name

    def LifeRecoveryfromFlasks_mid(self):
        Jew_name = '药剂恢复效果中型'
        test = [['Distilled Perfection', 'pre'],
                ['Spiked Concoction', 'pre'],
                ['Fasting', 'pre'],
                ["Mender's Wellspring", 'pre'],
                ['Special Reserve', 'pre'],
                ['Numbing Elixir', 'pre'],
                ]
        return test, Jew_name
