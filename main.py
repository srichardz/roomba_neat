import pygame
import neat
import yaml
import roomba
import sys, os

config = yaml.safe_load(open("config.yaml"))
course = pygame.image.load("course.png")

PPU    =  config["ppu"]
HEIGHT =  config["HEIGHT"]
WIDTH  =  config["WIDTH"]

pygame.init()

win = pygame.display.set_mode((HEIGHT*PPU, WIDTH*PPU))

clock = pygame.time.Clock()
ticks = 60

test_subjects = []      # the roombas
genomes = []
nets = []

def remove(index):
    test_subjects.pop(index)
    genomes.pop(index)
    nets.pop(index)

def eval_genomes(genomes, net_config):
    # create roombas
    for genome_id, genome in genomes:
        test_subjects.append(roomba.Roomba())
        genomes.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, net_config)
        nets.append(net)
        genome.fitness = 0

    run = True
    while run:
        # time
        dt = clock.get_time() / 1000

        # exit function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # draw the course
        win.blit(course, (0, 0))


        # check whether the population died out
        if len(test_subjects) == 0:
            break

        # tick and clear screen
        clock.tick(ticks)
        pygame.display.flip()

def run(config_path):
    global pop

    net_config = neat.config.Config(
        neat.DefaultGenome, 
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path
    )

    pop = neat.Population(net_config)

    pop.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)

    pop.run(eval_genomes, 50)

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, "config.txt")
    run(config_path)