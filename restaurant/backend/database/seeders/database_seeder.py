from database.seeders import OrderSeeder

SEEDERS = [
    OrderSeeder,
]


def main():
    for seeder in SEEDERS:
        seeder.run()


if __name__ == '__main__':
    main()
