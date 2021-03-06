from flask_restful import Resource, reqparse, fields

class UserDto:
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('mobile', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

class AuthDto:
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

class StockDto:
    parser = reqparse.RequestParser()
    parser.add_argument('symbol', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('company_name', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('series', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('listing_date', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('isin_number', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('face_value', type=int, required=True, help='This field cannot be left blank')
    parser.add_argument('company_detail', type=str, help='Company Detail')
    parser.add_argument('comapany_website', type=str, help='Company Website')