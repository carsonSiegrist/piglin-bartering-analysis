# Piglin Drop Rate Analysis Tool

## Description

Program outputs for Java and Bedrock editions are available at the end.

This script calculates statistics about Piglin Bartering in Mincraft. The script tells you the probability of each drop as a percentage, the expected number of items that each drop will give you, and the averge number of drops per barter the Piglin will provide. Furthermore, it calculates the average gold ingot cost of 1 of each item.  
The script was created based on the bartering rates from the [minecraft fandom wiki](https://minecraft.fandom.com/wiki/Bartering), accessed 11/5/2025, for game version Java 1.21.10.

I created this script to aid me in creating a bartering farm for my world, and I wanted to find out how many hoppers I needed per Piglin. The script takes the drop rate/second of Piglin bartering at maximum efficiency (technically possible, but very unlikely to actually be achieved) and compares it to hopper speed. Note that these are averages, and likely to fluctuate per barter - you may want make sure if you are applying this that you do not optimize for 100% hopper usage, you may consider accounting for some wiggle room in case of an unlucky series of large drops.

## Assumptions

I have relied on the wiki for my data, and I did not verify it. Furthermore, I have assumed that the item count ranges are uniform without verification. (i.e. if the range is 1-2, I assume 1 and 2 have an equal chance of being the dropped quantity)

## Reading Output

The program outputs a table, as well as some summary statistics. The table has the following labels:

- Item
  - The name of the item being bartered for
- p_i
  - The probability of the item being dropped, as a percentage. (I.e. 0.01 indicates a 1% chance to drop on a given barter)
- E[count]
  - The expected number of items you will recieve on average if that item is selected
- p_i\*E[count]
  - Measures the contribution to the average item drop rate. This is a measure of items.
- avg_cost
  - The average amount of gold ingots required to get one of the specified item.

## Usage

Simply run the script using Python. It doesn't take any parameters, but depending on your edition, you may want to change the T (timer per barter) variable. It should be set to 6 for Java, and 8 for Bedrock.

## Java 1.21.10 Output

Item p_i E[count] p_i\*E[count] avg_cost

| Item             | pᵢ      | E[count] | pᵢ·E[count] | Avg Cost |
|------------------|---------:|----------:|-------------:|---------:|
| Soul_Speed       | 0.0109  | 1.00      | 0.011        | 91.800   |
| Iron_Boots       | 0.0174  | 1.00      | 0.017        | 57.375   |
| Fire_Res         | 0.0174  | 1.00      | 0.017        | 57.375   |
| Fire_Res_Splash  | 0.0174  | 1.00      | 0.017        | 57.375   |
| Water_Bottle     | 0.0218  | 1.00      | 0.022        | 45.900   |
| Dried_Ghast      | 0.0218  | 1.00      | 0.022        | 45.900   |
| Iron_Nugget      | 0.0218  | 23.00     | 0.501        | 1.996    |
| Ender_Pearl      | 0.0218  | 3.00      | 0.065        | 15.300   |
| String           | 0.0436  | 6.00      | 0.261        | 3.825    |
| Quartz           | 0.0436  | 8.50      | 0.370        | 2.700    |
| Obsidian         | 0.0871  | 1.00      | 0.087        | 11.475   |
| Crying_Obsidian  | 0.0871  | 2.00      | 0.174        | 5.737    |
| Fire_Charge      | 0.0871  | 1.00      | 0.087        | 11.475   |
| Leather          | 0.0871  | 3.00      | 0.261        | 3.825    |
| Soul_Sand        | 0.0871  | 5.00      | 0.436        | 2.295    |
| Nether_Brick     | 0.0871  | 5.00      | 0.436        | 2.295    |
| Spectral_Arrow   | 0.0871  | 9.00      | 0.784        | 1.275    |
| Gravel           | 0.0871  | 12.00     | 1.046        | 0.956    |
| Blackstone       | 0.0871  | 12.00     | 1.046        | 0.956    |

Summary:  
Expected items per barter: 5.662  
Expected items per second: 0.944  
Expected items per minute: 56.6  
Hopper load fraction: 37.7% of one hopper capacity  

## Bedrock 1.21.120

Note: I do not play bedrock, and the only differences I am aware of in this care is that piglins take 8 seconds to barter compared to Java's 6, and that arrows are dropped instead of spectral arrows.

| Item             | pᵢ      | E[count] | pᵢ·E[count] | Avg Cost |
|------------------|---------:|----------:|-------------:|---------:|
| Soul_Speed       | 0.0109  | 1.00      | 0.011        | 91.800   |
| Iron_Boots       | 0.0174  | 1.00      | 0.017        | 57.375   |
| Fire_Res         | 0.0174  | 1.00      | 0.017        | 57.375   |
| Fire_Res_Splash  | 0.0174  | 1.00      | 0.017        | 57.375   |
| Water_Bottle     | 0.0218  | 1.00      | 0.022        | 45.900   |
| Dried_Ghast      | 0.0218  | 1.00      | 0.022        | 45.900   |
| Iron_Nugget      | 0.0218  | 23.00     | 0.501        | 1.996    |
| Ender_Pearl      | 0.0218  | 3.00      | 0.065        | 15.300   |
| String           | 0.0436  | 6.00      | 0.261        | 3.825    |
| Quartz           | 0.0436  | 8.50      | 0.370        | 2.700    |
| Obsidian         | 0.0871  | 1.00      | 0.087        | 11.475   |
| Crying_Obsidian  | 0.0871  | 2.00      | 0.174        | 5.737    |
| Fire_Charge      | 0.0871  | 1.00      | 0.087        | 11.475   |
| Leather          | 0.0871  | 3.00      | 0.261        | 3.825    |
| Soul_Sand        | 0.0871  | 5.00      | 0.436        | 2.295    |
| Nether_Brick     | 0.0871  | 5.00      | 0.436        | 2.295    |
| Arrow            | 0.0871  | 9.00      | 0.784        | 1.275    |
| Gravel           | 0.0871  | 12.00     | 1.046        | 0.956    |
| Blackstone       | 0.0871  | 12.00     | 1.046        | 0.956    |

Summary:  
Expected items per barter: 5.662  
Expected items per second: 0.708  
Expected items per minute: 42.5  
Hopper load fraction: 28.3% of one hopper capacity  
