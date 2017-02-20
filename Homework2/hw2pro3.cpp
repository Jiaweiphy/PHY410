#include <iostream>
#include <string>
#include <vector>
#include <iterator>
#include <algorithm>

int main()
{
	std::string myentree;
	std::string myside;
	std::string mybeverage;
	std::vector<std::string> entree{ "e1", "e2", "e3" };
	std::vector<std::string> side{ "s1", "s2", "s3" };
	std::vector<std::string> beverage{ "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8" };
	std::vector<std::string> entreemenu{ "Veggie burger", "Falafel Wrap", "Salami sandwich" };
	std::vector<std::string> sidemenu{ "French fries", "Hummus with pita chips", "Celery and carrots" };
	std::vector<std::string> beveragemenu{ "Tap water", "Sparkling water", "Domestic beer", "Imported beer", "Red wine", "White wine", "Coffee", "Tea" };
	int entreeprice[] = { 7, 6, 9 };
	int sideprice[] = { 2, 3, 2 };
	int beverageprice[] = { 0, 2, 4, 6, 7, 7, 1, 1 };
	int i, j, k;
	int totalprice;

	std::cout << std::endl
		      << "Entrees" << std::endl
              << entree[0] << " " << entreemenu[0] << " " << "$" << entreeprice[0] << std::endl
			  << entree[1] << " " << entreemenu[1] << " " << "$" << entreeprice[1] << std::endl
			  << entree[2] << " " << entreemenu[2] << " " << "$" << entreeprice[2] << std::endl
			  << "Sides" << std::endl
			  << side[0] << " " << sidemenu[0] << " " << "$" << sideprice[0] << std::endl
			  << side[1] << " " << sidemenu[1] << " " << "$" << sideprice[1] << std::endl
			  << side[2] << " " << sidemenu[2] << " " << "$" << sideprice[2] << std::endl
			  << "Beverages" << std::endl
			  << beverage[0] << " " << beveragemenu[0] << " " << "$" << beverageprice[0] << std::endl
			  << beverage[1] << " " << beveragemenu[1] << " " << "$" << beverageprice[1] << std::endl
			  << beverage[2] << " " << beveragemenu[2] << " " << "$" << beverageprice[2] << std::endl
			  << beverage[3] << " " << beveragemenu[3] << " " << "$" << beverageprice[3] << std::endl
			  << beverage[4] << " " << beveragemenu[4] << " " << "$" << beverageprice[4] << std::endl
			  << beverage[5] << " " << beveragemenu[5] << " " << "$" << beverageprice[5] << std::endl
			  << beverage[6] << " " << beveragemenu[6] << " " << "$" << beverageprice[6] << std::endl
			  << beverage[7] << " " << beveragemenu[7] << " " << "$" << beverageprice[7] << std::endl;

	std::cin >> myentree;
	if (std::find(std::begin(entree), std::end(entree), myentree) != std::end(entree))
		for (i = 0; i <= 2; i++) {
			if (myentree == entree[i]) {
				std::cin >> myside;
				if (std::find(std::begin(side), std::end(side), myside) != std::end(side))
					for (j = 0; j <= 2; j++) {
						if (myside == side[j]) {
							std::cin >> mybeverage;
							if (std::find(std::begin(beverage), std::end(beverage), mybeverage) != std::end(beverage))
								for (k = 0; k <= 7; k++) {
									if (mybeverage == beverage[k]) {
										totalprice = entreeprice[i] + sideprice[j] + beverageprice[k];
										if (i == 0) {
											if (j == 0) {
												if (k == 0) {
													std::cout << "You ordered a special combo, which costs $8." << std::endl;
												}
												else if (k == 1) {
													std::cout << "You ordered a special combo, which costs $8." << std::endl;
												}
												else if (k == 6) {
													std::cout << "You ordered a special combo, which costs $8." << std::endl;
												}
												else if (k == 7) {
													std::cout << "You ordered a special combo, which costs $8." << std::endl;
												}
												else
													std::cout << "The total price you need to pay is $" << totalprice << "." << std::endl;
											}
											else
												std::cout << "The total price you need to pay is $" << totalprice << "." << std::endl;
										}
										else if (i == 1) {
											if (j == 1) {
											    if (k == 6) {
													std::cout << "You ordered a special combo, which costs $7." << std::endl;
												}
												else if (k == 7) {
													std::cout << "You ordered a special combo, which costs $7." << std::endl;
												}
												else
													std::cout << "The total price you need to pay is $" << totalprice << "." << std::endl;
											}
											else
												std::cout << "The total price you need to pay is $" << totalprice << "." << std::endl;
										}
										else if (i == 2) {
											if (k == 2) {
												std::cout << "You ordered a special combo, which costs $13." << std::endl;
											}
											else if (k == 3) {
												std::cout << "You ordered a special combo, which costs $13." << std::endl;
											}
											else if (k == 4) {
												std::cout << "You ordered a special combo, which costs $13." << std::endl;
											}
											else if (k == 5) {
												std::cout << "You ordered a special combo, which costs $13." << std::endl;
											}
											else
												std::cout << "The total price you need to pay is $" << totalprice << "." << std::endl;
										}
									}
								}
							else
								std::cout << "I couldn't recognize your order." << std::endl;
						}
					}
				else
					std::cout << "I couldn't recognize your order." << std::endl;
			}
		}
	else
		std::cout << "I couldn't recognize your order." << std::endl;
    return 0;
}

