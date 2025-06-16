---
layout: post
title: Value Functions of Our Mind
categories: Reinforcement-Learning Psychology
---

My journey into RL has begun at its end: where it meets neuropsychology. In the midst of a technical book, I found that machines and humans really are not so different. 

Forgoing all mathematical details, in Reinforcement Learning, an agent must learn to maximize a reward in an uncertain environment. These programs are composed by subelements: 
- **Reward signal:** If the agent does something well, he obtains a reward.  
- **Value function:** Long term reward, this is where it gets interesting. An action could maximize short-term rewards and diminish the long-term reward. 
- **Policy:** This defines what actions the agent takes at each step.
- **Model of the environment:** How does the environment look like? 

And, of course, the agent.

As any human being, the agent will seek actions that maximize the reward at any given moment (yes, this depends on its policy). 

If this is something you can relate to when reaching for that ice cream late at night it's because Reinforcement Learning truly is the love child of Behavioral Psychology and Mathematics. 

# The road not taken

In this tryout of "making the best possible decision under uncertainty", RL faces the same issues as we do.

Imagine you're new to a city and you eat out every single night, trying to find the best restaurant. Each night you have the same question: "where should I go for dinner?". RL can help you make that decision (choose your Policy):

### A) Pure Exploitation

Always go to your favorite restaurant. Nevermind if there's a better choice out there. Of course, the first times you WILL have to explore, you don't know any restaurants yet! (Or you could trust the reviews).

### B) Balanced Strategy

Go to your favorite restaurant from Monday through Friday and to a new restaurant on the weekends. 

### C) Pure Exploration

Try a different restaurant every night. You'll discover amazing places, but also endure some terrible meals.

Depending on your Policy (or how you make decisions), you will feel risky or take the safe choice. This is the exploration-exploitation dilemma, and it's everywhere in human behavior. Should you stay in your current job or apply for that risky startup position? Should you stick with your proven investment strategy or try something new? Should you keep reading the same genre of books or venture into uncharted literary territory?

# The fundamental problem

The most basic agent in RL is the multi-armed bandit—imagine a casino with multiple slot machines, each with different (unknown) payout rates. You have a limited budget, so each pull matters. Do you keep pulling the machine that gave you the best result so far, or do you try the others to see if they're even better?

This seemingly simple problem captures the essence of learning under uncertainty. In the restaurant example, each restaurant is a "bandit arm" with its own hidden probability of satisfying you. Your challenge is to figure out which restaurants are worth your time while not missing out on potentially amazing discoveries.

What makes this fascinating is that humans face multi-armed bandit problems constantly, yet we're remarkably bad at solving them optimally. We tend to under-explore when young (missing opportunities) and over-explore when older (when we should be leveraging our experience). We get stuck in local optima, that decent restaurant we always go to, while missing the exceptional one two blocks away.

The multi-armed bandit problem teaches us that the cost of learning is real, but so is the cost of not learning. In a world of infinite restaurants, books, careers, and possibilities, perhaps the most human thing we can do is embrace both the uncertainty and the opportunity that comes with each choice.

# The regret we live with

In RL, there's a beautiful concept called "regret": the difference between the rewards you actually received and the rewards you could have gotten had you made optimal decisions. It's not emotional; it's mathematical. But doesn't it feel familiar?

Every time you think "I should have tried that restaurant sooner" or "I wish I'd invested in that stock earlier", you're experiencing regret. The difference is that RL agents are designed to minimize regret systematically, while humans often live with it, trapped by our suboptimal policies and **biased world models**.

The most successful people seem to intuitively understand these RL principles. They explore enough to discover opportunities but exploit enough to capitalize on what works. They update their beliefs based on evidence rather than emotion. They think in terms of long-term value functions rather than immediate rewards.

# What we can learn from machines

The beauty of this connection isn't that we should become more machine-like, but that we can become more aware of our decision-making patterns. When you catch yourself always ordering the same dish at a restaurant, ask: "Am I under-exploring?" When you find yourself constantly switching jobs without building expertise, wonder: "Am I over-exploring?"

The goal isn't to optimize your life like a machine. It's to understand the beautiful, messy, very human algorithms that are already running in our minds, and maybe, just maybe, to tune them a little better.
