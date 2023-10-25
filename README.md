# SMACrossoverTradingStrategy
This project implements and evaluates a simple moving average (SMA) crossover trading strategy on Apple Inc.'s stock (AAPL). The aim is to understand the effectiveness and potential profitability of this strategy over a specific historical period.

## Dataset
- Data Source: Yahoo Finance
- Time Period: January 1, 2018 - January 1, 2023
- Data Points: Daily closing prices

## Methodology
1. **Data Retrieval**: Utilized `yfinance` to fetch historical daily closing prices for AAPL.
2. **SMA Calculation**: Computed 50-day and 200-day SMAs for AAPL.
3. **Signal Generation**: Identified buy and sell signals based on SMA crossovers.
   - **Buy Signal**: Occurs when the 50-day SMA crosses above the 200-day SMA.
   - **Sell Signal**: Occurs when the 50-day SMA crosses below the 200-day SMA.
4. **Backtesting**: Simulated the trading strategy to evaluate potential profitability over the historical data period.

## Results
- Total Return: XX%
- Number of Trades: XX
- Maximum Drawdown: XX%

*(Replace XX with your actual results after implementation.)*

## Visualization
The project includes a visualization of AAPL's stock price, the two SMAs, and the buy/sell signals over the specified period.

## Future Work
- Explore the impact of transaction costs on profitability.
- Test and analyze the strategy on other stocks or asset classes.
- Refine the strategy by incorporating other technical indicators or adjusting SMA periods.

## Dependencies
- Python
- Pandas
- Matplotlib
- yfinance

## Author
[Your Name]

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

*(If you have a LICENSE file in your repo, you can link it. Otherwise, you can remove the License section.)*
