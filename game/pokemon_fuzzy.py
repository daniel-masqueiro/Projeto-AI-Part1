import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

'''
Cria um sistema Fuzzy que recebe como input a diferença dos niveis
e o efeito do ataque e devolve como input a probabilidade de ganhar
'''
# TO DO-Feito

level_input = ctrl.Antecedent(np.arange(-10, 11, 1), 'level_input')
level_input['Muito Abaixo'] = fuzz.trapmf(level_input.universe, [-10, -10, -5, -2])
level_input['Equilibrado']=fuzz.trimf(level_input.universe, [-5,0,5])
level_input['Muito Alto'] = fuzz.trapmf(level_input.universe, [2, 5, 10, 10])

effect_input = ctrl.Antecedent(np.arange(0, 2.1, 0.1), 'effect_input')
effect_input['Não Eficaz'] = fuzz.trapmf(effect_input.universe, [0, 0, 0.2, 0.5])
effect_input['Neutro']=fuzz.trimf(effect_input.universe, [0.5,1,2])
effect_input['Eficaz'] = fuzz.trapmf(effect_input.universe, [1.5, 2, 2, 2])

win_prob = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'win_prob')
win_prob['Baixa'] = fuzz.trimf(win_prob.universe, [0, 0, 0.5])
win_prob['Média'] = fuzz.trimf(win_prob.universe, [0, 0.5, 1])
win_prob['Alta'] = fuzz.trimf(win_prob.universe, [0.5, 1, 1])

regra1 = ctrl.Rule(level_input['Muito Abaixo'] & effect_input['Não Eficaz'], win_prob['Baixa'])
regra2 = ctrl.Rule(level_input['Muito Abaixo'] & effect_input['Neutro'], win_prob['Baixa'])
regra3 = ctrl.Rule(level_input['Muito Abaixo'] & effect_input['Eficaz'], win_prob['Média'])
regra4 = ctrl.Rule(level_input['Equilibrado'] & effect_input['Não Eficaz'], win_prob['Baixa'])
regra5 = ctrl.Rule(level_input['Equilibrado'] & effect_input['Neutro'], win_prob['Média'])
regra6 = ctrl.Rule(level_input['Equilibrado'] & effect_input['Eficaz'], win_prob['Alta'])
regra7 = ctrl.Rule(level_input['Muito Alto'] & effect_input['Não Eficaz'], win_prob['Média'])
regra8 = ctrl.Rule(level_input['Muito Alto'] & effect_input['Neutro'], win_prob['Alta'])
regra9 = ctrl.Rule(level_input['Muito Alto'] & effect_input['Eficaz'], win_prob['Alta'])

sistema_combate = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
simulacao = ctrl.ControlSystemSimulation(sistema_combate)

def calculate_prob(level_input, effect_input):
    simulacao.input['level_input'] = level_input
    simulacao.input['effect_input'] = effect_input
    simulacao.compute()
    return simulacao.output['win_prob']
    


