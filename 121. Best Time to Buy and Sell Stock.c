int maxProfit(int* prices, int pricesSize) {
    
    if (pricesSize < 2) {
        return 0;
    }

    int minPrice =
        prices[0];     
    int maxProfit = 0; 

    for (int i = 1; i < pricesSize; i++) {
        
        if (prices[i] < minPrice) {
            minPrice = prices[i];
        }

        
        int potentialProfit = prices[i] - minPrice;

        if (potentialProfit > maxProfit) {
            maxProfit = potentialProfit;
        }
    }

    return maxProfit;
}