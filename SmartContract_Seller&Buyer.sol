pragma solidity ^0.5.0;

contract CarSaleContract {
    struct Car {
        string model;
        uint256 year;
        uint256 mileage;
        uint256 salePrice;
        address payable seller;
        bool isSold;
    }

    Car[] public cars;

    event CarAdded(uint256 carId);
    // event CarSold(uint256 carId, address buyer, address seller);
    event CarSold(uint256 carId, address buyer);

    function addCar(string memory _model, uint256 _year, uint256 _mileage, uint256 _salePrice) public {
        Car memory newCar = Car({
            model: _model,
            year: _year,
            mileage: _mileage,
            salePrice: _salePrice,
            seller: msg.sender,
            isSold: false
        });

        uint256 carId = cars.length;
        cars.push(newCar);

        emit CarAdded(carId);
    }

    function buyCar(uint256 _carId) public payable {
        require(_carId < cars.length, "Invalid car ID");
        Car storage car = cars[_carId];

        require(!car.isSold, "Car is already sold");
        require(msg.value >= car.salePrice, "Insufficient payment");

        car.isSold = true;
        emit CarSold(_carId, msg.sender);

        if (msg.value > car.salePrice) {
            uint256 refundAmount = msg.value - car.salePrice;
            // payable(msg.sender).transfer(refundAmount);
            msg.sender.transfer(refundAmount);
        }

        // payable(car.seller).transfer(car.salePrice);
        car.seller.transfer(car.salePrice);
    }

    function getCarDetails(uint256 _carId) public view returns (string memory, uint256, uint256, uint256, address, bool) {
        require(_carId < cars.length, "Invalid car ID");
        Car storage car = cars[_carId];

        return (
            car.model,
            car.year,
            car.mileage,
            car.salePrice,
            car.seller,
            car.isSold
        );
    }

    function getNumberOfCars() public view returns (uint256) {
        return cars.length;
    }
}