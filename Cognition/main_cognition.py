__author__ = 'root'
import spacial_cognition
import temporal_cognition


def do(region):
    spa_cog = spacial_cognition.SpacialCognitor(region)
    winner  = spa_cog.do()
    spa_cog.print_winners()

    tem_cog = temporal_cognition.TemporalCognitor(region, winner)
    tem_cog.do()
