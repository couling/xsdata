from dataclasses import dataclass, field
from typing import List

from ..common_v48_0.common import *


@dataclass
class CustomerSearch:
    """
    Detailed customer information for searching pre pay profiles
    """

    pass


@dataclass
class ActionDetails:
    """
    Information related to the storing of the fare: Agent, Date and Action for Provider: 1P/1J
    """

    pseudo_city_code: TypePcc = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="PCC in the host of the agent who stored the fare for Provider: 1P/1J",
        )
    )
    agent_sine: str = field(
        default=None,
        metadata=dict(
            name="AgentSine",
            type="Attribute",
            help="The sign in of the user who stored the fare for Provider: 1P/1J",
        )
    )
    event_date: str = field(
        default=None,
        metadata=dict(
            name="EventDate",
            type="Attribute",
            help="Date at which the fare was stored for Provider: 1P/1J",
        )
    )
    event_time: str = field(
        default=None,
        metadata=dict(
            name="EventTime",
            type="Attribute",
            help="Time at which the fare was stored for Provider: 1P/1J",
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help="The type of action the agent performed for Provider: 1P/1J",
        )
    )


@dataclass
class AdditionalInfo:
    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="The category code is the code the AdditionalInfo text came from, e.g. S5 or S7.",
            required=True
        )
    )


@dataclass
class AddlBookingCodeInformation(TypeNonBlanks):
    """
    Returns additional booking codes for the selected fare
    """

    pass


@dataclass
class Adjustment:
    """
    An indentifier which indentifies adjustment made on original pricing. It can a flat amount or percentage of original price. The value of Amount/Percent can be negetive. Negative value implies a discount.
    """

    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Element",
            help="Implies a flat amount to be adjusted. Negetive value implies a discount.",
            required=True
        )
    )
    percent: float = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Element",
            help="Implies an adjustment to be made on original price. Negetive value implies a discount.",
            required=True
        )
    )
    adjusted_total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="AdjustedTotalPrice",
            type="Attribute",
            help="The adjusted price after applying adjustment on Total price",
            required=True
        )
    )
    approximate_adjusted_total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateAdjustedTotalPrice",
            type="Attribute",
            help="The Converted adjusted total price in Default Currency for this entity.",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Reference to a booking traveler for which adjustment is applied.",
        )
    )


@dataclass
class Advtype:
    adv_rsvn_only_if_tk: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnOnlyIfTk",
            type="Attribute",
            help="Reservation only if ticketed. True is advanced reservations only if tickets. False is no advanced reservations",
        )
    )
    adv_rsvn_any_tm: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnAnyTm",
            type="Attribute",
            help="Reservation anytime. True if advanced reservatiosn anytime. False if advanced reservations for a limited time.",
        )
    )
    adv_rsvn_hrs: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnHrs",
            type="Attribute",
            help="Reservation hours. True if advanced reservation time in hours. False if advanced reservation time not in hours.",
        )
    )
    adv_rsvn_days: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnDays",
            type="Attribute",
            help="Reservation days. True if advanced reservation time in days. False if advanced reservation time not in days.",
        )
    )
    adv_rsvn_months: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnMonths",
            type="Attribute",
            help="Reservation months. True if advanced reservation time in months. False if advanced reservation time not in months.",
        )
    )
    adv_rsvn_earliest_tm: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnEarliestTm",
            type="Attribute",
            help="Earliest reservation time. True if advanced reservations time is earliest permitted. False is advanced reservation time not earliest permitted time.",
        )
    )
    adv_rsvn_latest_tm: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnLatestTm",
            type="Attribute",
            help="Latest reservation time. True if advanced reservations time is latest permitted. False is advanced reservation time not latest permitted time.",
        )
    )
    adv_rsvn_waived: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnWaived",
            type="Attribute",
            help="Reservation Waived. True if advanced reservation waived. False if advanced reservation not waived.",
        )
    )
    adv_rsvn_data_exists: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnDataExists",
            type="Attribute",
            help="Reservation data exists. True if advanced reservation data exists. False if advanced reservation data does not exist.",
        )
    )
    adv_rsvn_end_item: bool = field(
        default=None,
        metadata=dict(
            name="AdvRsvnEndItem",
            type="Attribute",
            help="Reservation end item. True if advanced reservation end item and more values. False if it does not exist.",
        )
    )
    adv_tk_earliest_tm: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkEarliestTm",
            type="Attribute",
            help="Earliest ticketing time. True if earliest permitted. False if not earliest permitted.",
        )
    )
    adv_tk_latest_tm: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkLatestTm",
            type="Attribute",
            help="Latest ticketing time. True if time is latest permitted. False if time is not latest permitted.",
        )
    )
    adv_tk_rsvn_hrs: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnHrs",
            type="Attribute",
            help="Ticketing reservation hours. True if in hours. False if not in hours.",
        )
    )
    adv_tk_rsvn_days: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnDays",
            type="Attribute",
            help="Ticketing reservation days. True if in days. False if not in days.",
        )
    )
    adv_tk_rsvn_months: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnMonths",
            type="Attribute",
            help="Ticketing reservation months. True if in months. False if not in months.",
        )
    )
    adv_tk_start_hrs: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkStartHrs",
            type="Attribute",
            help="Latest ticketing departure. True if time is latest permitted. False if time is not latest permitted.",
        )
    )
    adv_tk_start_days: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkStartDays",
            type="Attribute",
            help="Ticketing departure days. True if in days. False if not in days.",
        )
    )
    adv_tk_start_months: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkStartMonths",
            type="Attribute",
            help="Ticketing reservation months. True if in months. False if not in months.",
        )
    )
    adv_tk_waived: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkWaived",
            type="Attribute",
            help="Ticketing waived. True if waived. False if not waived.",
        )
    )
    adv_tk_any_tm: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkAnyTm",
            type="Attribute",
            help="Ticketing anytime. True if anytime. False if limited time.",
        )
    )
    adv_tk_end_item: bool = field(
        default=None,
        metadata=dict(
            name="AdvTkEndItem",
            type="Attribute",
            help="Ticketing end item. True if advanced ticketing item and more values. False if end item does not exist.",
        )
    )
    adv_rsvn_tm: int = field(
        default=None,
        metadata=dict(
            name="AdvRsvnTm",
            type="Attribute",
            help="Advanced reservation time.",
        )
    )
    adv_tk_rsvn_tm: int = field(
        default=None,
        metadata=dict(
            name="AdvTkRsvnTm",
            type="Attribute",
            help="Advanced ticketing reservation time.",
        )
    )
    adv_tk_start_tm: int = field(
        default=None,
        metadata=dict(
            name="AdvTkStartTm",
            type="Attribute",
            help="Advanced ticketing departure time.",
        )
    )
    earliest_rsvn_dt_present: bool = field(
        default=None,
        metadata=dict(
            name="EarliestRsvnDtPresent",
            type="Attribute",
            help="Earliest reservation date. True if date is present. False if date is not present.",
        )
    )
    earliest_tk_dt_present: bool = field(
        default=None,
        metadata=dict(
            name="EarliestTkDtPresent",
            type="Attribute",
            help="Earliest ticketing date. True if date is present. False if date is not present.",
        )
    )
    latest_rsvn_dt_present: bool = field(
        default=None,
        metadata=dict(
            name="LatestRsvnDtPresent",
            type="Attribute",
            help="Latest reservation date. True if date is present. False if date is not present.",
        )
    )
    latest_tk_dt_present: bool = field(
        default=None,
        metadata=dict(
            name="LatestTkDtPresent",
            type="Attribute",
            help="Latest ticketing date. True if date is present. False if date is not present.",
        )
    )
    earliest_rsvn_dt: str = field(
        default=None,
        metadata=dict(
            name="EarliestRsvnDt",
            type="Attribute",
            help="Earliest reservation date.",
        )
    )
    earliest_tk_dt: str = field(
        default=None,
        metadata=dict(
            name="EarliestTkDt",
            type="Attribute",
            help="Earliest ticketing date.",
        )
    )
    latest_rsvn_dt: str = field(
        default=None,
        metadata=dict(
            name="LatestRsvnDt",
            type="Attribute",
            help="Latest reservation date.",
        )
    )
    latest_tk_dt: str = field(
        default=None,
        metadata=dict(
            name="LatestTkDt",
            type="Attribute",
            help="Latest ticketing date.",
        )
    )


@dataclass
class AirFareDisplayRuleKey(TypeNonBlanks):
    """
    The Tariff Fare Rule requested using a Key. The key is typically a provider specific string which is required to make either a following Air Fare Tariff request for Mileage/Routing information or Air Fare Tariff Rule Request.
    """

    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirItinerarySolutionRef:
    """
    Reference to a complete AirItinerarySolution from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class AirPricingInfoRef:
    """
    Reference to a AirPricing from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class AirRefundInfo:
    """
    Provides results of a refund quote
    """

    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata=dict(
            name="RefundRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute",
            help=None,
        )
    )
    retain_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RetainAmount",
            type="Attribute",
            help=None,
        )
    )
    refund_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RefundFee",
            type="Attribute",
            help="Refund fee for ACH/1P",
        )
    )
    refundable_taxes: str = field(
        default=None,
        metadata=dict(
            name="RefundableTaxes",
            type="Attribute",
            help="1P - None : All taxes are not refundable. Unknown : Refundability of taxes are not known.",
        )
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            help="1P Currency of filed CAT33 refund fee",
        )
    )
    conversion_rate: float = field(
        default=None,
        metadata=dict(
            name="ConversionRate",
            type="Attribute",
            help="1P - Currency conversion rate used for conversion between FiledCurrency and PCC base currency in which the response is returned.",
        )
    )
    taxes: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help="1P - The total value of taxes.",
        )
    )
    original_ticket_total: TypeMoney = field(
        default=None,
        metadata=dict(
            name="OriginalTicketTotal",
            type="Attribute",
            help="1P - The original ticket amount.",
        )
    )
    forfeit_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute",
            help=None,
        )
    )
    retain: bool = field(
        default="false",
        metadata=dict(
            name="Retain",
            type="Attribute",
            help="This indicates whether any amount is retained by the provider.",
        )
    )
    refund: bool = field(
        default="false",
        metadata=dict(
            name="Refund",
            type="Attribute",
            help="This indicates whether carrier/host supports refund for the correcponding pnr.",
        )
    )


@dataclass
class AirReservationLocatorCode(TypeLocatorCode):
    """
    Identifies the AirReservation LocatorCode within the Universal Record
    """

    pass


@dataclass
class AirSearchAsynchModifiers:
    """
    Controls and switches for the Air Search request for Asynch Request
    """

    initial_asynch_result: "AirSearchAsynchModifiers.InitialAsynchResult" = field(
        default=None,
        metadata=dict(
            name="InitialAsynchResult",
            type="Element",
            help=None,
        )
    )

    @dataclass
    class InitialAsynchResult:
        max_wait: int = field(
            default=None,
            metadata=dict(
                name="MaxWait",
                type="Attribute",
                help="Max wait time in seconds.",
            )
        )


@dataclass
class AirSegmentRef:
    """
    Reference to a complete AirSegment from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class AirSegmentTicketingModifiers:
    """
    Specifies modifiers that a particular segment should be priced with. If this is used, then there must be one for each AirSegment in the AirItinerary.
    """

    air_segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute",
            help=None,
        )
    )
    brand_tier: StringLength1to10 = field(
        default=None,
        metadata=dict(
            name="BrandTier",
            type="Attribute",
            help="Modifier to price by specific brand tier number.",
            required=True
        )
    )


@dataclass
class Alliance:
    """
    Alliance Code
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The possible values are *A for Star Alliance,*O for One world,*S for Sky team etc.",
            required=True
        )
    )


@dataclass
class AlternateLocationDistance:
    """
    Information about the Original Search Airport to Alternate Search Airport.
    """

    distance: Distance = field(
        default=None,
        metadata=dict(
            name="Distance",
            type="Element",
            help=None,
            required=True
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    search_location: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="SearchLocation",
            type="Attribute",
            help="The Searching City or Airport specified in the Request.",
            required=True
        )
    )
    alternate_location: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="AlternateLocation",
            type="Attribute",
            help="The nearby Alternate City or Airport to SearchLocation.",
            required=True
        )
    )


@dataclass
class AlternateLocationDistanceRef:
    """
    Reference to a AlternateLocationDistance
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class AssociatedRemark(TypeAssociatedRemarkWithSegmentRef):
    pass


@dataclass
class AsyncProviderSpecificResponse(BaseAsyncProviderSpecificResponse):
    """
    Identifies pending responses from a specific provider using MoreResults attribute
    """

    pass


@dataclass
class AttrLinkInfo:
    """
    Holds Participant Level information.
    """

    participant_level: str = field(
        default=None,
        metadata=dict(
            name="ParticipantLevel",
            type="Attribute",
            help="Type of sell agreement between host and link carrier.",
        )
    )
    link_availability: bool = field(
        default=None,
        metadata=dict(
            name="LinkAvailability",
            type="Attribute",
            help="Indicates if carrier has link (carrier specific) display option.",
        )
    )
    polled_availability_option: str = field(
        default=None,
        metadata=dict(
            name="PolledAvailabilityOption",
            type="Attribute",
            help="Indicates if carrier has Inside (polled)Availability option.",
        )
    )
    availability_display_type: str = field(
        default=None,
        metadata=dict(
            name="AvailabilityDisplayType",
            type="Attribute",
            help="The type of availability from which the segment is sold.Possible Values (List): G - General S - Flight Specific L - Carrier Specific/Direct Access M - Manual Sell F - Fare Shop/Optimal Shop Q - Fare Specific Fare Quote unbooked R - Redemption Availability used to complete the sell. Supported Providers: 1G,1V.",
        )
    )


@dataclass
class AttrPolicyMarking:
    in_policy: bool = field(
        default=None,
        metadata=dict(
            name="InPolicy",
            type="Attribute",
            help="This attribute will be used to indicate if a fare or rate has been determined to be ‘in policy’ based on the associated policy settings.",
        )
    )
    preferred_option: bool = field(
        default=None,
        metadata=dict(
            name="PreferredOption",
            type="Attribute",
            help="This attribute is used to indicate if the vendors responsible for the fare or rate being returned have been determined to be ‘preferred’ based on the associated policy settings.",
        )
    )


@dataclass
class AutoSeatAssignment:
    """
    Request object used to request seats automatically by seat type
    """

    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="The segment that this assignment belongs to",
        )
    )
    smoking: bool = field(
        default="false",
        metadata=dict(
            name="Smoking",
            type="Attribute",
            help="Indicates that the requested seat type should be a smoking seat.",
        )
    )
    seat_type: TypeReqSeat = field(
        default=None,
        metadata=dict(
            name="SeatType",
            type="Attribute",
            help="The type of seat that is requested",
            required=True
        )
    )
    group: bool = field(
        default="false",
        metadata=dict(
            name="Group",
            type="Attribute",
            help="Indicates that this seat request is for group seating for all passengers. If no SegmentRef is included, group seating will be requested for all segments.",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="The booking traveler that this seat assignment is for. If not entered, this applies to the primary booking traveler and other passengers are adjacent.",
        )
    )


@dataclass
class AvailableDiscount:
    loyalty_program: List[LoyaltyProgram] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyProgram",
            type="Element",
            help="Customer Loyalty Program Detail.",
            min_occurs=0,
            max_occurs=999
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
        )
    )
    percent: TypePercentageWithDecimal = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Attribute",
            help=None,
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help=None,
        )
    )
    discount_qualifier: str = field(
        default=None,
        metadata=dict(
            name="DiscountQualifier",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AvailableSsr:
    """
    A wrapper for all the information regarding each of the available SSR
    """

    ssr: List[Ssr] = field(
        default_factory=list,
        metadata=dict(
            name="SSR",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ssrrules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata=dict(
            name="SSRRules",
            type="Element",
            help="Holds the rules for selecting the SSR in the itinerary",
            min_occurs=0,
            max_occurs=999
        )
    )
    industry_standard_ssr: List[IndustryStandardSsr] = field(
        default_factory=list,
        metadata=dict(
            name="IndustryStandardSSR",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BookingCode:
    """
    The Booking Code (Class of Service) for a segment
    """

    code: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class BookingCodeInfo:
    """
    Details Cabin class info and class of service information with availability counts. Only provided on search results and grouped by Cabin class
    """

    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.",
        )
    )
    booking_counts: str = field(
        default=None,
        metadata=dict(
            name="BookingCounts",
            type="Attribute",
            help="Lists class of service and their counts for specific cabin class",
        )
    )


@dataclass
class BookingInfo:
    """
    Links segments and fares together
    """

    booking_code: str = field(
        default=None,
        metadata=dict(
            name="BookingCode",
            type="Attribute",
            help=None,
            required=True
        )
    )
    booking_count: str = field(
        default=None,
        metadata=dict(
            name="BookingCount",
            type="Attribute",
            help="Seat availability of the BookingCode",
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help=None,
        )
    )
    fare_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help=None,
            required=True
        )
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help=None,
        )
    )
    coupon_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="CouponRef",
            type="Attribute",
            help="The coupon to which that booking is relative (if applicable)",
        )
    )
    air_itinerary_solution_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirItinerarySolutionRef",
            type="Attribute",
            help="Reference to an Air Itinerary Solution",
        )
    )
    host_token_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute",
            help="HostToken Reference for this segment and fare combination.",
        )
    )


@dataclass
class BrandId:
    """
    Brand ids for Merchandising details.
    """

    id: str = field(
        default=None,
        metadata=dict(
            name="Id",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class BrandModifiers:
    """
    Used to specify the level of branding requested.
    """

    fare_family_display: "BrandModifiers.FareFamilyDisplay" = field(
        default=None,
        metadata=dict(
            name="FareFamilyDisplay",
            type="Element",
            help="Used to request a fare family display.",
            required=True
        )
    )
    basic_details_only: "BrandModifiers.BasicDetailsOnly" = field(
        default=None,
        metadata=dict(
            name="BasicDetailsOnly",
            type="Element",
            help="Used to request basic details of the brand.",
            required=True
        )
    )

    @dataclass
    class FareFamilyDisplay:
        modifier_type: str = field(
            default=None,
            metadata=dict(
                name="ModifierType",
                type="Attribute",
                help="'FareFamily' returns the lowest branded fares in a fare family. 'MaintainBookingCode' attempts to return the lowest branded fare in a fare family display based on the permitted booking code. Any brand that does not have a fare for the permitted booking code will then have the lowest fare returned. 'LowestFareInBrand' returns the lowest fare within each branded fare in a fare family display.",
                required=True
            )
        )

    @dataclass
    class BasicDetailsOnly:
        return_basic_details: bool = field(
            default=None,
            metadata=dict(
                name="ReturnBasicDetails",
                type="Attribute",
                help=None,
                required=True
            )
        )


@dataclass
class CarrierCode(TypeCarrier):
    pass


@dataclass
class Co2Emission:
    """
    Carbon emission values
    """

    air_segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute",
            help="The segment reference",
        )
    )
    value: float = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help="The CO2 emission value for the air segment",
        )
    )


@dataclass
class CodeshareInfo(str):
    """
    Describes the codeshare disclosure (simple text string) or the specific operating flight information (as attributes).
    """

    operating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="OperatingCarrier",
            type="Attribute",
            help="The actual carrier that is operating the flight.",
        )
    )
    operating_flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="OperatingFlightNumber",
            type="Attribute",
            help="The actual flight number of the carrier that is operating the flight.",
        )
    )


@dataclass
class CompanyName:
    """
    Supplier info that is specific to the Unique Id
    """

    supplier_code: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class ConjunctedTicketInfo:
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            required=True
        )
    )
    iatanumber: TypeIata = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            help=None,
        )
    )
    ticket_issue_date: str = field(
        default=None,
        metadata=dict(
            name="TicketIssueDate",
            type="Attribute",
            help=None,
        )
    )
    ticketing_agent_sign_on: str = field(
        default=None,
        metadata=dict(
            name="TicketingAgentSignOn",
            type="Attribute",
            help=None,
            max_length=8.0
        )
    )
    country_code: TypeCountry = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            help="Contains Ticketed PCC’s Country code.",
        )
    )
    status: TypeTicketStatus = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class ContractCode(AttrProviderSupplier):
    """
    Some private fares (non-ATPCO) are secured to a contract code.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The 1-64 character string which uniquely identifies a Contract.",
            required=True,
            min_length=1.0,
            max_length=64.0
        )
    )
    company_name: str = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Attribute",
            help="Providers supported : ACH",
        )
    )


@dataclass
class CreditSummary:
    """
    Credit summary associated with the account
    """

    currency_code: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            help=None,
        )
    )
    current_balance: float = field(
        default=None,
        metadata=dict(
            name="CurrentBalance",
            type="Attribute",
            help=None,
            required=True
        )
    )
    initial_credit: float = field(
        default=None,
        metadata=dict(
            name="InitialCredit",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class CustomerReceiptInfo:
    """
    Information about customer receipt via email. Supported providers are 1V/1G/1P/1J
    """

    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Refererence of the Booking Traveler related to the email.",
            required=True
        )
    )
    email_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="EmailRef",
            type="Attribute",
            help="Reference to the email address used for receipt of EMD.",
            required=True
        )
    )


@dataclass
class Document:
    """
    APIS Document Details.
    """

    sequence: int = field(
        default=None,
        metadata=dict(
            name="Sequence",
            type="Attribute",
            help="Sequence number for the document.",
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of the Document. Visa, Passport, DriverLicense etc.",
        )
    )
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            help="Applicability level of the Document. Required, Supported, API_Supported or Unknown.",
        )
    )


@dataclass
class DocumentModifiers:
    generate_itinerary_invoice: bool = field(
        default="false",
        metadata=dict(
            name="GenerateItineraryInvoice",
            type="Attribute",
            help="Generate itinerary/invoice documents along with ticket",
        )
    )
    generate_accounting_interface: bool = field(
        default="false",
        metadata=dict(
            name="GenerateAccountingInterface",
            type="Attribute",
            help="Generate interface message along with ticket",
        )
    )


@dataclass
class DocumentRequired:
    """
    Additional Details, Documents , Project IDs
    """

    doc_type: str = field(
        default=None,
        metadata=dict(
            name="DocType",
            type="Attribute",
            help=None,
        )
    )
    include_exclude_use_ind: bool = field(
        default=None,
        metadata=dict(
            name="IncludeExcludeUseInd",
            type="Attribute",
            help=None,
        )
    )
    doc_id: str = field(
        default=None,
        metadata=dict(
            name="DocId",
            type="Attribute",
            help=None,
        )
    )
    allowed_ids: str = field(
        default=None,
        metadata=dict(
            name="AllowedIds",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Embargo:
    """
    Embargo details. Provider: 1G, 1V, 1P, 1J
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
        )
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help=None,
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="The commercial name of the optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
            max_length=30.0
        )
    )
    text: str = field(
        default=None,
        metadata=dict(
            name="Text",
            type="Attribute",
            help="Brief description of the embargo. Provider: 1G, 1V, 1P, 1J",
        )
    )
    secondary_type: str = field(
        default=None,
        metadata=dict(
            name="SecondaryType",
            type="Attribute",
            help="The secondary type of the optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
        )
    )
    type: TypeMerchandisingService = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The type of optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
        )
    )
    url: str = field(
        default=None,
        metadata=dict(
            name="Url",
            type="Attribute",
            help="Website of the operating carrier. Provider: 1G, 1V, 1P, 1J",
        )
    )
    service_sub_code: str = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            help="The service sub code of the optional service on which the embargo applies. Provider: 1G, 1V, 1P, 1J",
            max_length=3.0
        )
    )


@dataclass
class Emdcommission:
    """
    Commission information to be used for EMD issuance. Supported providers are 1V/1G/1P/1J
    """

    type: TypeAdjustmentType = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of the commission applied.One of Amount/Percentage",
            required=True
        )
    )
    value: float = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help="Value of the commission applied for EMD issuance.Could represent amount or percentage depending on the type",
            required=True
        )
    )
    currency_code: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="CurrencyCode",
            type="Attribute",
            help="Currency of the commission amount applied.Applicable only with type - Amount",
        )
    )


@dataclass
class Emdcoupon(AttrElementKeyResults):
    """
    The coupon information for the EMD issued. Supported providers are 1G/1V/1P/1J
    """

    number: int = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="Number of the EMD coupon",
            required=True
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Status of the coupon. Possible values Open, Void, Refunded, Exchanged, Irregular Operations,Airport Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown",
            required=True
        )
    )
    svc_description: str = field(
        default=None,
        metadata=dict(
            name="SvcDescription",
            type="Attribute",
            help="Description of the service related to the EMD Coupon",
        )
    )
    consumed_at_issuance_ind: bool = field(
        default=None,
        metadata=dict(
            name="ConsumedAtIssuanceInd",
            type="Attribute",
            help="Indicates if the EMD coupon has been considered used as soon as issued.",
        )
    )
    rfic: str = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute",
            help="Reason For Issuance Code for the EMD coupon",
            required=True,
            length=1
        )
    )
    rfisc: str = field(
        default=None,
        metadata=dict(
            name="RFISC",
            type="Attribute",
            help="Reason For Issueance Sub code for the EMD coupon",
        )
    )
    rfidescription: str = field(
        default=None,
        metadata=dict(
            name="RFIDescription",
            type="Attribute",
            help="Reason for Issueance Description for the EMD coupon",
            min_length=1.0,
            max_length=86.0
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Departure Airport Code for the flight with which the Coupon is associated",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Destination Airport Code for the flight with which the Coupon is associated",
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="Flight Number of the flight with which the coupon is associated.",
        )
    )
    present_to: str = field(
        default=None,
        metadata=dict(
            name="PresentTo",
            type="Attribute",
            help="Service provider to present the coupon to",
            min_length=1.0,
            max_length=71.0
        )
    )
    present_at: str = field(
        default=None,
        metadata=dict(
            name="PresentAt",
            type="Attribute",
            help="Location of service provider where this coupon should be presented at",
            min_length=1.0,
            max_length=71.0
        )
    )
    non_refundable_ind: bool = field(
        default=None,
        metadata=dict(
            name="NonRefundableInd",
            type="Attribute",
            help="Indicates whether the coupon is non-refundable",
        )
    )
    marketing_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="MarketingCarrier",
            type="Attribute",
            help="Marketing carrier associated with the coupon",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="System generated Key",
        )
    )


@dataclass
class Emdendorsement:
    """
    Endorsement for EMD. Supported providers are 1V/1G/1P/1J
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=255.0
        )
    )


@dataclass
class EmdtravelerInfo:
    """
    EMD traveler information. Supported providers are 1G/1V/1P/1J
    """

    name_info: "EmdtravelerInfo.NameInfo" = field(
        default=None,
        metadata=dict(
            name="NameInfo",
            type="Element",
            help="Name information of the EMD traveler.",
            required=True
        )
    )
    traveler_type: TypePtc = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            help="Defines the type of traveler used for booking which could be a non-defining type (Companion, Web-fare, etc), or a standard type (Adult, Child, etc).",
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            help="Age of the traveler",
        )
    )

    @dataclass
    class NameInfo(AttrBookingTravelerName):
        pass


@dataclass
class ExchangedTicketInfo:
    """
    Contains Exchanged/Reissued Ticket Information
    """

    number: TypeTicketNumber = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="Original Ticket that was Exchange/Reissued",
            required=True
        )
    )


@dataclass
class ExcludeTicketing:
    """
    Exclude ticketing of traveler referenced. Supported Provider: JAL.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference to a booking traveler for which ticketing modifier is applied.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class ExemptTaxes:
    """
    Request tax exemption for specific tax category and/or all taxes of a specific country
    """

    country_code: List[TypeCountry] = field(
        default_factory=list,
        metadata=dict(
            name="CountryCode",
            type="Element",
            help="Specify ISO country code for which tax exemption is requested.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_category: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="TaxCategory",
            type="Element",
            help="Specify tax category for which tax exemption is requested.",
            min_occurs=0,
            max_occurs=999
        )
    )
    all_taxes: bool = field(
        default=None,
        metadata=dict(
            name="AllTaxes",
            type="Attribute",
            help="Request exemption of all taxes.",
        )
    )
    tax_territory: str = field(
        default=None,
        metadata=dict(
            name="TaxTerritory",
            type="Attribute",
            help="exemption is achieved by sending in the TaxTerritory in the tax exempt price request.",
            length=2
        )
    )
    company_name: str = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Attribute",
            help="The federal government body name must be provided in this element. This field is required by AC",
            min_length=1.0,
            max_length=24.0
        )
    )


@dataclass
class FareBasis:
    """
    Fare Basis Code
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The fare basis code for this fare",
            required=True
        )
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="The segment to which this FareBasis Code is to connected",
        )
    )


@dataclass
class FareCalc(str):
    """
    The complete fare calculation line.
    """

    pass


@dataclass
class FareDetailsRef:
    """
    Reference of the Fare
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareInfoMessage(str):
    """
    A simple textual fare information message.Providers supported : 1G/1V/1P/1J
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareInfoRef:
    """
    Reference to a complete FareInfo from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareMileageInformation(str):
    """
    Contains Fare/Tariff Display Mileage Information
    """

    pass


@dataclass
class FareNote(str):
    """
    A simple textual fare note. Used within several other objects.
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    precedence: int = field(
        default=None,
        metadata=dict(
            name="Precedence",
            type="Attribute",
            help=None,
        )
    )
    note_name: str = field(
        default=None,
        metadata=dict(
            name="NoteName",
            type="Attribute",
            help=None,
        )
    )
    fare_info_message_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="FareInfoMessageRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareNoteRef:
    """
    A reference to a fare note from a shared list. Used to minimize xml results.
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FarePricing:
    """
    Container for Fare Pricing Information. One per PTC type.
    """

    passenger_type: TypePtc = field(
        default=None,
        metadata=dict(
            name="PassengerType",
            type="Attribute",
            help=None,
        )
    )
    total_fare_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalFareAmount",
            type="Attribute",
            help=None,
        )
    )
    private_fare: bool = field(
        default=None,
        metadata=dict(
            name="PrivateFare",
            type="Attribute",
            help="NegotiatedFare attribute from earlier version of schema used to imply whether the fare is private fare or not. So, this attribute is renamed to PrivateFare as it best suited.",
        )
    )
    negotiated_fare: bool = field(
        default=None,
        metadata=dict(
            name="NegotiatedFare",
            type="Attribute",
            help="Identifies the fare as a Negotiated Fare.",
        )
    )
    auto_priceable: bool = field(
        default=None,
        metadata=dict(
            name="AutoPriceable",
            type="Attribute",
            help="Identifies the fare as Autopriceable or not. False value means the fare filing is incomplete and the fare should not be used.",
        )
    )
    total_net_fare_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalNetFareAmount",
            type="Attribute",
            help="Total Net fare amount.",
        )
    )
    base_fare: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute",
            help="Base fare amount.",
        )
    )
    taxes: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help=None,
        )
    )
    mmid: TypeRef = field(
        default=None,
        metadata=dict(
            name="MMid",
            type="Attribute",
            help="Contains the Reference id which is generated when the request was ReturnMM=”true”.",
        )
    )


@dataclass
class FareRemarkRef:
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareRestrictionSaleDate:
    """
    Restrict when this fare can be sold
    """

    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help=None,
        )
    )
    end_date: str = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRestrictionSeasonal:
    """
    Fares Restricted based on the season requested. StartDate and EndDate are strings representing respective dates. If a year component is present then it signifies an exact date. If only day and month components are present then it signifies a seasonal date, which means applicable for that date in any year
    """

    comment: str = field(
        default=None,
        metadata=dict(
            name="Comment",
            type="Attribute",
            help=None,
        )
    )
    variation_by_travel_dates: str = field(
        default=None,
        metadata=dict(
            name="VariationByTravelDates",
            type="Attribute",
            help=None,
        )
    )
    seasonal_range1_ind: str = field(
        default=None,
        metadata=dict(
            name="SeasonalRange1Ind",
            type="Attribute",
            help=None,
        )
    )
    seasonal_range1_start_date: str = field(
        default=None,
        metadata=dict(
            name="SeasonalRange1StartDate",
            type="Attribute",
            help=None,
        )
    )
    seasonal_range1_end_date: str = field(
        default=None,
        metadata=dict(
            name="SeasonalRange1EndDate",
            type="Attribute",
            help=None,
        )
    )
    seasonal_range2_ind: str = field(
        default=None,
        metadata=dict(
            name="SeasonalRange2Ind",
            type="Attribute",
            help=None,
        )
    )
    seasonal_range2_start_date: str = field(
        default=None,
        metadata=dict(
            name="SeasonalRange2StartDate",
            type="Attribute",
            help=None,
        )
    )
    seasonal_range2_end_date: str = field(
        default=None,
        metadata=dict(
            name="SeasonalRange2EndDate",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRoutingInformation(str):
    """
    Contains Fare/Tariff Display Routing Information
    """

    pass


@dataclass
class FareRuleCategory:
    """
    Rule Categories to filter on.
    """

    category: int = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help=None,
            required=True,
            min_inclusive=1.0,
            max_inclusive=50.0
        )
    )


@dataclass
class FareRuleKey(TypeNonBlanks):
    """
    The Fare Rule requested using a Key. The key is typically a provider specific string which is required to make a following Air Fare Rule Request. This Key is returned in Low Fare Shop or Air Price Response
    """

    fare_info_ref: str = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help="The Fare Component to which this Rule Key applies",
            required=True
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareRuleLong(str):
    """
    Long Text Fare Rule
    """

    category: int = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help=None,
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRuleLongRef:
    """
    A reference to an Long Text Rule in a Shared List
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareRuleLookup:
    """
    Parameters to use for a fare rule lookup that is not associated with an Air Reservation Locator Code.
    """

    account_code: AccountCode = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help=None,
        )
    )
    point_of_sale: PointOfSale = field(
        default=None,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            help=None,
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help=None,
            required=True
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help=None,
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
            required=True
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help=None,
            required=True
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
            required=True
        )
    )
    departure_date: str = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            help=None,
        )
    )
    ticketing_date: str = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRuleNameValue:
    """
    Fare Rule Name Value Pair, used in Short Rules
    """

    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help=None,
            required=True
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareRuleShortRef:
    """
    A reference to an Short Text Rule in a Shared List
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareRulesFilterCategory:
    """
    Fare Rules Filter if requested will return rules for requested category in the response. Applicable for providers 1G,1V,1P,1J.
    """

    category_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryCode",
            type="Element",
            help="Fare Rules Filter category can be requested. Currently only '˜MIN, MAX, ADV, CHG, OTH' is supported. Applicable for Providers 1G,1V,1P,1J.",
            min_occurs=1,
            max_occurs=35
        )
    )
    fare_info_ref: str = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help="This tells if Low Fare Finder was used.",
        )
    )


@dataclass
class FareStatusFailureInfo:
    """
    Denotes the failure reason of a particular fare.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The failure code of the fare.",
            required=True
        )
    )
    reason: str = field(
        default=None,
        metadata=dict(
            name="Reason",
            type="Attribute",
            help="The reason for the failure.",
        )
    )


@dataclass
class FareSurcharge(AttrElementKeyResults):
    """
    Surcharges for a fare component
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
            required=True
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help=None,
        )
    )
    coupon_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="CouponRef",
            type="Attribute",
            help="The coupon to which that surcharge is relative (if applicable)",
        )
    )


@dataclass
class FeeInfo(TypeFeeInfo):
    """
    A generic type of fee for those charges which are incurred by the passenger, but not necessarily shown on tickets
    """

    pass


@dataclass
class FlexExploreModifiers:
    """
    This is the container for a set of modifiers which allow the user to perform a special kind of low fare search, depicted as flex explore, based on different parameters like Area, Zone, Country, State, Specific locations, Distance around the actual destination of the itinerary. Applicable for providers 1G,1V,1P
    """

    destination: List[TypeIatacode] = field(
        default_factory=list,
        metadata=dict(
            name="Destination",
            type="Element",
            help="List of specific destinations for performing flex explore. Applicable only with flex explore type - Destination",
            min_occurs=0,
            max_occurs=59
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of flex explore to be performed",
            required=True
        )
    )
    radius: int = field(
        default=None,
        metadata=dict(
            name="Radius",
            type="Attribute",
            help="Radius around the destination of actual itinerary in which the search would be performed. Supported only with types - DistanceInMiles and DistanceInKilometers",
        )
    )
    group_name: str = field(
        default=None,
        metadata=dict(
            name="GroupName",
            type="Attribute",
            help="Group name for a set of destinations to be searched. Use with Type=Group. Group names are defined in the Search Control Console. Supported Providers: 1G/1V/1P",
            max_length=15.0
        )
    )


@dataclass
class FlightDetailsRef:
    """
    Reference to a complete FlightDetails from a shared list
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FlightInfoCriteria:
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="An identifier to link the flightinfo responses to the criteria. The value passed here will be returned in the resulting flightinfo(s) from this command.",
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="The carrier that is marketing this segment",
            required=True
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="The flight number under which the marketing carrier is marketing this flight",
            required=True
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
        )
    )
    departure_date: str = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            help="The date at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FlightType:
    """
    Modifier to request flight type options example non-stop only, non-stop and direct only, include single online connection etc.
    """

    require_single_carrier: bool = field(
        default="false",
        metadata=dict(
            name="RequireSingleCarrier",
            type="Attribute",
            help=None,
        )
    )
    max_connections: int = field(
        default="-1",
        metadata=dict(
            name="MaxConnections",
            type="Attribute",
            help="The maximum number of connections within a segment group.",
            min_inclusive=-1.0,
            max_inclusive=3.0
        )
    )
    max_stops: int = field(
        default="-1",
        metadata=dict(
            name="MaxStops",
            type="Attribute",
            help="The maximum number of stops within a connection.",
            min_inclusive=-1.0,
            max_inclusive=3.0
        )
    )
    non_stop_directs: bool = field(
        default=None,
        metadata=dict(
            name="NonStopDirects",
            type="Attribute",
            help=None,
        )
    )
    stop_directs: bool = field(
        default=None,
        metadata=dict(
            name="StopDirects",
            type="Attribute",
            help=None,
        )
    )
    single_online_con: bool = field(
        default=None,
        metadata=dict(
            name="SingleOnlineCon",
            type="Attribute",
            help=None,
        )
    )
    double_online_con: bool = field(
        default=None,
        metadata=dict(
            name="DoubleOnlineCon",
            type="Attribute",
            help=None,
        )
    )
    triple_online_con: bool = field(
        default=None,
        metadata=dict(
            name="TripleOnlineCon",
            type="Attribute",
            help=None,
        )
    )
    single_interline_con: bool = field(
        default=None,
        metadata=dict(
            name="SingleInterlineCon",
            type="Attribute",
            help=None,
        )
    )
    double_interline_con: bool = field(
        default=None,
        metadata=dict(
            name="DoubleInterlineCon",
            type="Attribute",
            help=None,
        )
    )
    triple_interline_con: bool = field(
        default=None,
        metadata=dict(
            name="TripleInterlineCon",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class GroupedOption:
    optional_service_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="OptionalServiceRef",
            type="Attribute",
            help="Reference to a optionalService which is paired with other optional services in the parent PairedOptions element.",
            required=True
        )
    )


@dataclass
class HostReservation:
    """
    Defines a reservation that already exists in the host system (e.g an agent using Galileo Desktop already booked a reservation on Midwest in Sabre host system).
    """

    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="The carrier code (e.g. YX, UA, ...) that is providing the merchandising",
            required=True
        )
    )
    carrier_locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="CarrierLocatorCode",
            type="Attribute",
            help="The locator code in the supplier system (also could be defined as locator in the carrier host system).",
            required=True
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the GDS or other provider code of the entity actually housing the reservation. This is optional when used on Merchandising Availability but required on MerchandisingFulfillment.",
            required=True
        )
    )
    provider_locator_code: TypeProviderLocatorCode = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Contains the locator of the reservation actually housed in the provider.",
            required=True
        )
    )
    universal_locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="UniversalLocatorCode",
            type="Attribute",
            help="The locator of the Universal Record, if one exists.",
        )
    )
    eticket: bool = field(
        default="false",
        metadata=dict(
            name="ETicket",
            type="Attribute",
            help="An flag to indicate if ticket has been issued for the PNR.",
        )
    )


@dataclass
class HostTokenList:
    """
    The shared object list of Host Tokens
    """

    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class ImageLocation(str):
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of Image Location. E.g., 'Agent', 'Consumer'.",
            required=True
        )
    )
    image_width: int = field(
        default=None,
        metadata=dict(
            name="ImageWidth",
            type="Attribute",
            help="The width of the image",
            required=True
        )
    )
    image_height: int = field(
        default=None,
        metadata=dict(
            name="ImageHeight",
            type="Attribute",
            help="The height of the image",
            required=True
        )
    )


@dataclass
class InFlightServices(str):
    """
    Available InFlight Services. They are: 'Movie', 'Telephone', 'Telex', 'AudioProgramming', 'Television' ,'ResvBookingService' ,'DutyFreeSales' ,'Smoking' ,'NonSmoking' ,'ShortFeatureVideo' ,'NoDutyFree' ,'InSeatPowerSource' ,'InternetAccess' ,'Email' ,'Library' ,'LieFlatSeat' ,'Additional service(s) exists' ,'WiFi' ,'Lie-Flat seat first' ,'Lie-Flat seat business' ,'Lie-Flat seat premium economy' ,'Amenities subject to change' etc.. These follow the IATA standard. Please see the IATA standards for a more complete list.
    """

    pass


@dataclass
class LanguageOption:
    """
    Enables itineraries and invoices to print in different languages.
    """

    language: TypeLanguage = field(
        default=None,
        metadata=dict(
            name="Language",
            type="Attribute",
            help="2 Letter ISO Language code",
            required=True
        )
    )
    country: TypeCountry = field(
        default=None,
        metadata=dict(
            name="Country",
            type="Attribute",
            help="2 Letter ISO Country code",
            required=True
        )
    )


@dataclass
class LegDetail:
    """
    Information about the journey Leg, Shared by Leg and LegPrice Elements
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    origin_airport: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="OriginAirport",
            type="Attribute",
            help="Returns the origin airport code for the Leg Detail.",
            required=True
        )
    )
    destination_airport: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="DestinationAirport",
            type="Attribute",
            help="Returns the destination airport code for the Leg Detail.",
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="Carrier for the Search Leg Detail.",
            required=True
        )
    )
    travel_date: str = field(
        default=None,
        metadata=dict(
            name="TravelDate",
            type="Attribute",
            help="The Departure date and time for this Leg Detail.",
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="Flight Number for the Search Leg Detail.",
        )
    )


@dataclass
class LegRef:
    """
    Reference to a Leg
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class LoyaltyCardDetails:
    """
    Passenger Loyalty card details
    """

    supplier_code: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Carrier Code",
            required=True
        )
    )
    priority_code: TypePriorityCode = field(
        default=None,
        metadata=dict(
            name="PriorityCode",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class MaxLayoverDurationRangeType:
    """
    Layover duration range of valid values 0-9999
    """

    value: int = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_inclusive=0.0,
            max_inclusive=9999.0
        )
    )


@dataclass
class Maxtype:
    hours_max: bool = field(
        default=None,
        metadata=dict(
            name="HoursMax",
            type="Attribute",
            help="Maximum hours. True if unit of time is hours. False if unit of time is not hours.",
        )
    )
    days_max: bool = field(
        default=None,
        metadata=dict(
            name="DaysMax",
            type="Attribute",
            help="Maximum days. True if unit of time is days. False if unit of time is not days.",
        )
    )
    months_max: bool = field(
        default=None,
        metadata=dict(
            name="MonthsMax",
            type="Attribute",
            help="Maximum months. True if unit of time is months. False if unit of time is not months.",
        )
    )
    occur_ind_max: bool = field(
        default=None,
        metadata=dict(
            name="OccurIndMax",
            type="Attribute",
            help="Maximum cccurance indicator. True if day of the week is used. False if day of the week is not used.",
        )
    )
    same_day_max: bool = field(
        default=None,
        metadata=dict(
            name="SameDayMax",
            type="Attribute",
            help="Same day maximum. True if Stay is same day. False if Stay is not same day.",
        )
    )
    start_ind_max: bool = field(
        default=None,
        metadata=dict(
            name="StartIndMax",
            type="Attribute",
            help="Start indicator. True if start indicator. False if not a start indicator.",
        )
    )
    completion_ind: bool = field(
        default=None,
        metadata=dict(
            name="CompletionInd",
            type="Attribute",
            help="Completion indicator. True if Completion C Indicator. False if not Completion C Indicator.",
        )
    )
    tm_dowmax: int = field(
        default=None,
        metadata=dict(
            name="TmDOWMax",
            type="Attribute",
            help="If a max unit of time is true then number corrolates to day of the week starting with 1 for Sunday.",
        )
    )
    num_occur_max: int = field(
        default=None,
        metadata=dict(
            name="NumOccurMax",
            type="Attribute",
            help="Number of maximum occurances.",
        )
    )


@dataclass
class MerchandisingPricingModifiers:
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help="The account code is used to get corporate discounted pricing on paid seats. Provider:ACH",
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class Mintype:
    hours_min: bool = field(
        default=None,
        metadata=dict(
            name="HoursMin",
            type="Attribute",
            help="Minimum hours. True if unit of time is hours. False if unit of time is not hours.",
        )
    )
    days_min: bool = field(
        default=None,
        metadata=dict(
            name="DaysMin",
            type="Attribute",
            help="Minimum days. True if unit of time is days. False if unit of time is not days.",
        )
    )
    months_min: bool = field(
        default=None,
        metadata=dict(
            name="MonthsMin",
            type="Attribute",
            help="Minimum months. True if unit of time is months. False if unit of time is not months.",
        )
    )
    occur_ind_min: bool = field(
        default=None,
        metadata=dict(
            name="OccurIndMin",
            type="Attribute",
            help="Minimum occurance indicator. True if day of the week is used. False if day of the week is not used.",
        )
    )
    same_day_min: bool = field(
        default=None,
        metadata=dict(
            name="SameDayMin",
            type="Attribute",
            help="Same day minimum. True if Stay is same day. False if Stay is not same day.",
        )
    )
    tm_dowmin: int = field(
        default=None,
        metadata=dict(
            name="TmDOWMin",
            type="Attribute",
            help="If a min unit of time is true then number corrolates to day of the week starting with 1 for Sunday.",
        )
    )
    fare_component: int = field(
        default=None,
        metadata=dict(
            name="FareComponent",
            type="Attribute",
            help="Fare component number of the most restrictive fare.",
        )
    )
    num_occur_min: int = field(
        default=None,
        metadata=dict(
            name="NumOccurMin",
            type="Attribute",
            help="Number of min occurances. This field is used in conjunction with the Day of Week.",
        )
    )


@dataclass
class MultiGdssearchIndicator:
    """
    Indicates whether public fares and/or private fares should be returned.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Indicates whether only public fares or both public and private fares should be returned or a specific type of private fares. Examples of valid values are PublicFaresOnly, PrivateFaresOnly, AirlinePrivateFaresOnly, AgencyPrivateFaresOnly, PublicandPrivateFares, and NetFaresOnly.",
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
        )
    )
    default_provider: bool = field(
        default=None,
        metadata=dict(
            name="DefaultProvider",
            type="Attribute",
            help="Use the value “true” if the provider is the default (primary) provider. Use the value “false” if the provider is the alternate (secondary). Use of this attribute requires specifically provisioned credentials.",
        )
    )
    private_fare_code: str = field(
        default=None,
        metadata=dict(
            name="PrivateFareCode",
            type="Attribute",
            help="The code of the corporate private fare. This is the same as an account code. Use of this attribute requires specifically provisioned credentials.",
        )
    )
    private_fare_code_only: bool = field(
        default=None,
        metadata=dict(
            name="PrivateFareCodeOnly",
            type="Attribute",
            help=": Indicates whether or not the private fares returned should be restricted to only those specific to the PrivateFareCode in the previous attribute. This has the same validation as the AccountCodeFaresOnly attribute. Use of this attribute requires specifically provisioned credentials.",
        )
    )


@dataclass
class OfferAvailabilityModifiers:
    service_type: List[TypeMerchandisingService] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceType",
            type="Element",
            help="To restrict offers to only this type.",
            min_occurs=0,
            max_occurs=999
        )
    )
    carrier: List[TypeCarrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            help="The carrier whose paid seat optional services is to be returned by uAPI.",
            min_occurs=0,
            max_occurs=999
        )
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help="Currency code override. Providers: ACH, 1G, 1V, 1P, 1J",
        )
    )


@dataclass
class OptionalServiceModifier:
    """
    Optional service modifiers
    """

    type: TypeMerchandisingService = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Optional service type",
            required=True
        )
    )
    secondary_type: TypeMerchandisingService = field(
        default=None,
        metadata=dict(
            name="SecondaryType",
            type="Attribute",
            help="Secondary optional service type",
        )
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Optional service supplier code",
            required=True
        )
    )
    service_sub_code: str = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            help="As published by ATPCO",
            required=True
        )
    )
    travel_date: str = field(
        default=None,
        metadata=dict(
            name="TravelDate",
            type="Attribute",
            help="The departure date of the air segment the optional service is valid for.",
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Attribute",
            help="This allows MDS to return specific image and text corresponding to the ancillary name (S5 ancillary name).",
            required=True
        )
    )


@dataclass
class OptionalServiceRef(TypeRef):
    """
    Reference to optional service
    """

    pass


@dataclass
class Othtype:
    cat0: bool = field(
        default=None,
        metadata=dict(
            name="Cat0",
            type="Attribute",
            help="Category 0 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat1: bool = field(
        default=None,
        metadata=dict(
            name="Cat1",
            type="Attribute",
            help="Category 1 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat2: bool = field(
        default=None,
        metadata=dict(
            name="Cat2",
            type="Attribute",
            help="Category 2 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat3: bool = field(
        default=None,
        metadata=dict(
            name="Cat3",
            type="Attribute",
            help="Category 3 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat4: bool = field(
        default=None,
        metadata=dict(
            name="Cat4",
            type="Attribute",
            help="Category 4 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat5: bool = field(
        default=None,
        metadata=dict(
            name="Cat5",
            type="Attribute",
            help="Category 5 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat6: bool = field(
        default=None,
        metadata=dict(
            name="Cat6",
            type="Attribute",
            help="Category 6 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat7: bool = field(
        default=None,
        metadata=dict(
            name="Cat7",
            type="Attribute",
            help="Category 7 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat8: bool = field(
        default=None,
        metadata=dict(
            name="Cat8",
            type="Attribute",
            help="Category 8 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat9: bool = field(
        default=None,
        metadata=dict(
            name="Cat9",
            type="Attribute",
            help="Category 9 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat10: bool = field(
        default=None,
        metadata=dict(
            name="Cat10",
            type="Attribute",
            help="Category 10 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat11: bool = field(
        default=None,
        metadata=dict(
            name="Cat11",
            type="Attribute",
            help="Category 11 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat12: bool = field(
        default=None,
        metadata=dict(
            name="Cat12",
            type="Attribute",
            help="Category 12 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat13: bool = field(
        default=None,
        metadata=dict(
            name="Cat13",
            type="Attribute",
            help="Category 13 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat14: bool = field(
        default=None,
        metadata=dict(
            name="Cat14",
            type="Attribute",
            help="Category 14 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat15: bool = field(
        default=None,
        metadata=dict(
            name="Cat15",
            type="Attribute",
            help="Category 15 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat16: bool = field(
        default=None,
        metadata=dict(
            name="Cat16",
            type="Attribute",
            help="Category 16 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat17: bool = field(
        default=None,
        metadata=dict(
            name="Cat17",
            type="Attribute",
            help="Category 17 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat18: bool = field(
        default=None,
        metadata=dict(
            name="Cat18",
            type="Attribute",
            help="Category 18 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat19: bool = field(
        default=None,
        metadata=dict(
            name="Cat19",
            type="Attribute",
            help="Category 19 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat20: bool = field(
        default=None,
        metadata=dict(
            name="Cat20",
            type="Attribute",
            help="Category 20 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat21: bool = field(
        default=None,
        metadata=dict(
            name="Cat21",
            type="Attribute",
            help="Category 21 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat22: bool = field(
        default=None,
        metadata=dict(
            name="Cat22",
            type="Attribute",
            help="Category 22 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat23: bool = field(
        default=None,
        metadata=dict(
            name="Cat23",
            type="Attribute",
            help="Category 23 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat24: bool = field(
        default=None,
        metadata=dict(
            name="Cat24",
            type="Attribute",
            help="Category 24 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat25: bool = field(
        default=None,
        metadata=dict(
            name="Cat25",
            type="Attribute",
            help="Category 25 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat26: bool = field(
        default=None,
        metadata=dict(
            name="Cat26",
            type="Attribute",
            help="Category 26 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat27: bool = field(
        default=None,
        metadata=dict(
            name="Cat27",
            type="Attribute",
            help="Category 27 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat28: bool = field(
        default=None,
        metadata=dict(
            name="Cat28",
            type="Attribute",
            help="Category 28 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat29: bool = field(
        default=None,
        metadata=dict(
            name="Cat29",
            type="Attribute",
            help="Category 29 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat30: bool = field(
        default=None,
        metadata=dict(
            name="Cat30",
            type="Attribute",
            help="Category 30 rules. True if category applies. False if rules do not apply.",
        )
    )
    cat31: bool = field(
        default=None,
        metadata=dict(
            name="Cat31",
            type="Attribute",
            help="Category 31 rules. True if category applies. False if rules do not apply.",
        )
    )
    restrictive_dt: str = field(
        default=None,
        metadata=dict(
            name="RestrictiveDt",
            type="Attribute",
            help="Most restrictive ticketing date.",
        )
    )
    surcharge_amt: float = field(
        default=None,
        metadata=dict(
            name="SurchargeAmt",
            type="Attribute",
            help="Surcharge amount",
        )
    )
    not_usacity: bool = field(
        default=None,
        metadata=dict(
            name="NotUSACity",
            type="Attribute",
            help="Not USA city. True if Origin or final destination not a continental U.S. City. False if Origin or final destination a continental U.S. City.",
        )
    )
    missing_rules: bool = field(
        default=None,
        metadata=dict(
            name="MissingRules",
            type="Attribute",
            help="Missing rules. True if rules are missing. False if rules are not missing.",
        )
    )


@dataclass
class OverrideCode:
    """
    Code corresponding to the type of OverridableException the user wishes to override.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            length=4
        )
    )


@dataclass
class PassengerDetailsRef:
    """
    Reference of the Passenger
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class PassengerReceiptOverride(TypeNonBlanks):
    """
    It is required when a passenger receipt is required immediately ,GDS overrides the default value
    """

    pass


@dataclass
class PassengerSeatPrice:
    """
    Only used when a passenger has a different price than the default.
    """

    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help=None,
            required=True
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class PaymentRef:
    """
    Reference to one of the air reservation payments
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class PenFeeType:
    dep_required: bool = field(
        default=None,
        metadata=dict(
            name="DepRequired",
            type="Attribute",
            help="Deposit required. True if require. False if not required.",
        )
    )
    dep_non_ref: bool = field(
        default=None,
        metadata=dict(
            name="DepNonRef",
            type="Attribute",
            help="Deposit non-refundable. True is non-refundanbe. False is refundable.",
        )
    )
    tk_non_ref: bool = field(
        default=None,
        metadata=dict(
            name="TkNonRef",
            type="Attribute",
            help="Ticket non-refundable. True if non-refundanbe. False if refundable.",
        )
    )
    air_vfee: bool = field(
        default=None,
        metadata=dict(
            name="AirVFee",
            type="Attribute",
            help="Carrier fee. True if carrier fee is assessed should passenger for complete all conditions for travel at fare. False if it does not exist.",
        )
    )
    cancellation: bool = field(
        default=None,
        metadata=dict(
            name="Cancellation",
            type="Attribute",
            help="Cancellation. True if subject to penalty. False if no penalty.",
        )
    )
    fail_confirm_space: bool = field(
        default=None,
        metadata=dict(
            name="FailConfirmSpace",
            type="Attribute",
            help="Failure to confirm space. True if subject to penalty if seats are not confirmed. False if subject to penalty if seats are confirmed.",
        )
    )
    itin_chg: bool = field(
        default=None,
        metadata=dict(
            name="ItinChg",
            type="Attribute",
            help="Subject to penalty if Itinerary is changed requiring reissue of ticket. True if subject to penalty. False if no penalty if reissue required.",
        )
    )
    replace_tk: bool = field(
        default=None,
        metadata=dict(
            name="ReplaceTk",
            type="Attribute",
            help="Replace ticket. True if subject to penalty, if replacement of lost ticket / exchange order. False if no penalty, if replacement of lost ticket or exchange order.",
        )
    )
    applicable: bool = field(
        default=None,
        metadata=dict(
            name="Applicable",
            type="Attribute",
            help="Applicable. True if amount specified is applicable. Flase if amount specified is not applicable.",
        )
    )
    applicable_to: bool = field(
        default=None,
        metadata=dict(
            name="ApplicableTo",
            type="Attribute",
            help="Applicable to penalty or deposit. True if amount specified applies to penalty. False if amount specified applies to deposit.",
        )
    )
    amt: float = field(
        default=None,
        metadata=dict(
            name="Amt",
            type="Attribute",
            help="Amount of penalty. If XXX.XX then it is an amount. If it is XX then is is a percenatge. Eg 100.00 or 000100.",
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of penalty. If it is D then dollar. If it is P then percentage.",
        )
    )
    currency: str = field(
        default=None,
        metadata=dict(
            name="Currency",
            type="Attribute",
            help="Currency code of penalty (e.g. USD).",
        )
    )


@dataclass
class Penalty:
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="Penalty Amount",
        )
    )
    penalty_type: str = field(
        default=None,
        metadata=dict(
            name="PenaltyType",
            type="Attribute",
            help="This is the PPC (Price Processing Code)code.",
        )
    )


@dataclass
class PenaltyInformation(str):
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="Fare-owning carrier",
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help="Unique identifier that provides the association to the fare amount and fare rules.",
        )
    )
    fare_component: int = field(
        default=None,
        metadata=dict(
            name="FareComponent",
            type="Attribute",
            help="A portion of a journey or itinerary between two consecutive fare break points.",
        )
    )
    priceable_unit: int = field(
        default=None,
        metadata=dict(
            name="PriceableUnit",
            type="Attribute",
            help="Identifies FareComponents that are priced together",
        )
    )
    board_point: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="BoardPoint",
            type="Attribute",
            help="Origin for the FareComponent",
        )
    )
    off_point: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="OffPoint",
            type="Attribute",
            help="Destination for the FareComponent",
        )
    )
    minimum_change_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="MinimumChangeFee",
            type="Attribute",
            help="Estimated minimum change fee associated with the fare component. Can be overridden by ChangeFeeApplicationCodes for other fare components.",
        )
    )
    maximum_change_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="MaximumChangeFee",
            type="Attribute",
            help="Estimated maximum change fee associated with the fare component. Can be overridden by ChangeFeeApplicationCodes for other fare components.",
        )
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            help="Currency of the filed change fee",
        )
    )
    conversion_rate: float = field(
        default=None,
        metadata=dict(
            name="ConversionRate",
            type="Attribute",
            help="Conversion rate from filed change fee currency to reissue location currency",
        )
    )
    refundable: bool = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            help="Answers whether the FareComponent is refundable",
        )
    )
    change_fee_application_code: str = field(
        default=None,
        metadata=dict(
            name="ChangeFeeApplicationCode",
            type="Attribute",
            help="Unique code associated with the PenaltyInformation text which defines how fees will be applied/calculated. E.g. J2 translates to 'From among all fare components, changed and unchanged....'",
            length=2
        )
    )


@dataclass
class PermittedCabins:
    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=5
        )
    )


@dataclass
class PermittedCarriers:
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class PersonName:
    """
    Customer name field
    """

    first: StringLength1to64 = field(
        default=None,
        metadata=dict(
            name="First",
            type="Attribute",
            help="Person First Name.",
        )
    )
    last: StringLength1to64 = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            help="Person Last Name.",
            required=True
        )
    )
    prefix: StringLength1to16 = field(
        default=None,
        metadata=dict(
            name="Prefix",
            type="Attribute",
            help="Person Name prefix.",
        )
    )


@dataclass
class PersonNameSearch:
    """
    Customer name field
    """

    last: StringLength1to64 = field(
        default=None,
        metadata=dict(
            name="Last",
            type="Attribute",
            help="Person Last Name to be searched for Flight Pass content.",
            required=True
        )
    )


@dataclass
class PocketItineraryRemark(TypeAssociatedRemarkWithSegmentRef):
    pass


@dataclass
class PolicyCodesList:
    policy_code: List[TypePolicyCode] = field(
        default_factory=list,
        metadata=dict(
            name="PolicyCode",
            type="Element",
            help="A code that indicates why an item was determined to be ‘out of policy’.",
            min_occurs=1,
            max_occurs=10
        )
    )


@dataclass
class PreferredCabins:
    cabin_class: CabinClass = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class PreferredCarriers:
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class PriceChangeType(str):
    """
    Indicates a price change is found in Fare Control Manager
    """

    amount: str = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="Contains the currency and amount information. Assume the amount is added unless a hyphen is present to indicate subtraction.",
            required=True
        )
    )
    carrier: str = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="Contains carrier code information",
        )
    )
    segment_ref: str = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="Contains segment reference information",
        )
    )


@dataclass
class PriceRange:
    default_currency: bool = field(
        default=None,
        metadata=dict(
            name="DefaultCurrency",
            type="Attribute",
            help="Indicates if the currency code of StartPrice / EndPrice is the default currency code",
        )
    )
    start_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="StartPrice",
            type="Attribute",
            help="Price range start value",
        )
    )
    end_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="EndPrice",
            type="Attribute",
            help="Price range end value",
        )
    )


@dataclass
class PricingDetails:
    """
    Used for rapid reprice. This is a response element. Additional information about how pricing was obtain, messages, etc. Providers: 1G/1V/1P/1S/1A
    """

    advisory_message: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="AdvisoryMessage",
            type="Element",
            help="Advisory messages returned from the host.",
            min_occurs=0,
            max_occurs=999
        )
    )
    endorsement_text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="EndorsementText",
            type="Element",
            help="Endorsement text returned from the host.",
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_text: str = field(
        default=None,
        metadata=dict(
            name="WaiverText",
            type="Element",
            help="Waiver text returned from the host.",
        )
    )
    low_fare_pricing: bool = field(
        default="false",
        metadata=dict(
            name="LowFarePricing",
            type="Attribute",
            help="This tells if Low Fare Finder was used.",
        )
    )
    low_fare_found: bool = field(
        default="false",
        metadata=dict(
            name="LowFareFound",
            type="Attribute",
            help="This tells if the lowest fare was found.",
        )
    )
    penalty_applies: bool = field(
        default="false",
        metadata=dict(
            name="PenaltyApplies",
            type="Attribute",
            help="This tells if penalties apply.",
        )
    )
    discount_applies: bool = field(
        default="false",
        metadata=dict(
            name="DiscountApplies",
            type="Attribute",
            help="This tells if a discount applies.",
        )
    )
    itinerary_type: TypeItineraryCode = field(
        default=None,
        metadata=dict(
            name="ItineraryType",
            type="Attribute",
            help="Values allowed are International or Domestic. This tells if the itinerary is international or domestic.",
        )
    )
    validating_vendor_code: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="ValidatingVendorCode",
            type="Attribute",
            help="The vendor code of the validating carrier.",
        )
    )
    for_ticketing_on_date: str = field(
        default=None,
        metadata=dict(
            name="ForTicketingOnDate",
            type="Attribute",
            help="The ticketing date of the itinerary.",
        )
    )
    last_date_to_ticket: str = field(
        default=None,
        metadata=dict(
            name="LastDateToTicket",
            type="Attribute",
            help="The last date to issue the ticket.",
        )
    )
    form_of_refund: TypeFormOfRefund = field(
        default=None,
        metadata=dict(
            name="FormOfRefund",
            type="Attribute",
            help="How the refund will be issued. Values will be MCO or FormOfPayment",
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help=None,
        )
    )
    bankers_selling_rate: float = field(
        default=None,
        metadata=dict(
            name="BankersSellingRate",
            type="Attribute",
            help="The selling rate at time of quote.",
        )
    )
    pricing_type: TypePricingType = field(
        default=None,
        metadata=dict(
            name="PricingType",
            type="Attribute",
            help="Ties with the RepricingModifiers sent in the request and tells how the itinerary was priced.",
        )
    )
    conversion_rate: float = field(
        default=None,
        metadata=dict(
            name="ConversionRate",
            type="Attribute",
            help="The conversion rate at the time of quote.",
        )
    )
    rate_of_exchange: float = field(
        default=None,
        metadata=dict(
            name="RateOfExchange",
            type="Attribute",
            help="The exchange rate at time of quote.",
        )
    )
    original_ticket_currency: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="OriginalTicketCurrency",
            type="Attribute",
            help="The currency of the original ticket.",
        )
    )


@dataclass
class PrintBlankFormItinerary:
    """
    Produce a customized itinerary/Invoice document in blank form format.
    """

    include_description: bool = field(
        default=None,
        metadata=dict(
            name="IncludeDescription",
            type="Attribute",
            help="If it is true then document will be printed including descriptions.",
            required=True
        )
    )
    include_header: bool = field(
        default=None,
        metadata=dict(
            name="IncludeHeader",
            type="Attribute",
            help="If it is true then document will be printed including it's header.",
            required=True
        )
    )


@dataclass
class ProhibitedCabins:
    cabin_class: List[CabinClass] = field(
        default_factory=list,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=3
        )
    )


@dataclass
class ProhibitedCarriers:
    carrier: List[Carrier] = field(
        default_factory=list,
        metadata=dict(
            name="Carrier",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class PromoCode:
    """
    A container to specify Promotional code with Provider code and Supplier code.
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="To be used to specify Promotional Code.",
            required=True,
            min_length=1.0,
            max_length=64.0
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="To be used to specify Provider Code.",
            required=True
        )
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="To be used to specify Supplier Code.",
            required=True
        )
    )


@dataclass
class RailCoachDetails:
    rail_coach_number: str = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute",
            help="Rail coach number for the returned coach details.",
        )
    )
    available_rail_seats: str = field(
        default=None,
        metadata=dict(
            name="AvailableRailSeats",
            type="Attribute",
            help="Number of available seats present in this rail coach.",
        )
    )
    rail_seat_map_availability: bool = field(
        default=None,
        metadata=dict(
            name="RailSeatMapAvailability",
            type="Attribute",
            help="Indicates if seats are available in this rail coach which can be mapped.",
        )
    )


@dataclass
class RefundAccessCode:
    """
    For some vendors a code/password is required to avail any amount retained during refund.User can define their own password too This attribute will be used to show/accept this code.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=32.0
        )
    )


@dataclass
class Restriction:
    """
    Fare Reference associated with the BookingRules
    """

    days_of_week_restriction: List["Restriction.DaysOfWeekRestriction"] = field(
        default_factory=list,
        metadata=dict(
            name="DaysOfWeekRestriction",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    restriction_passenger_types: List["Restriction.RestrictionPassengerTypes"] = field(
        default_factory=list,
        metadata=dict(
            name="RestrictionPassengerTypes",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class DaysOfWeekRestriction(AttrDow):
        restriction_exists_ind: bool = field(
            default=None,
            metadata=dict(
                name="RestrictionExistsInd",
                type="Attribute",
                help=None,
            )
        )
        application: str = field(
            default=None,
            metadata=dict(
                name="Application",
                type="Attribute",
                help=None,
            )
        )
        include_exclude_use_ind: bool = field(
            default=None,
            metadata=dict(
                name="IncludeExcludeUseInd",
                type="Attribute",
                help=None,
            )
        )

    @dataclass
    class RestrictionPassengerTypes:
        max_nbr_travelers: str = field(
            default=None,
            metadata=dict(
                name="MaxNbrTravelers",
                type="Attribute",
                help=None,
            )
        )
        total_nbr_ptc: str = field(
            default=None,
            metadata=dict(
                name="TotalNbrPTC",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class RoutingRules:
    """
    Rules related to routing
    """

    routing: List["RoutingRules.Routing"] = field(
        default_factory=list,
        metadata=dict(
            name="Routing",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class Routing:
        direction_info: List["RoutingRules.Routing.DirectionInfo"] = field(
            default_factory=list,
            metadata=dict(
                name="DirectionInfo",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=999
            )
        )
        routing_constructed_ind: bool = field(
            default=None,
            metadata=dict(
                name="RoutingConstructedInd",
                type="Attribute",
                help=None,
            )
        )
        number: str = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute",
                help=None,
            )
        )
        routing_restriction: str = field(
            default=None,
            metadata=dict(
                name="RoutingRestriction",
                type="Attribute",
                help=None,
            )
        )

        @dataclass
        class DirectionInfo:
            location_code: TypeIatacode = field(
                default=None,
                metadata=dict(
                    name="LocationCode",
                    type="Attribute",
                    help=None,
                )
            )
            direction: str = field(
                default=None,
                metadata=dict(
                    name="Direction",
                    type="Attribute",
                    help=None,
                )
            )


@dataclass
class RuleCharges:
    """
    Container for rules related to charges such as deposits, surcharges, penalities, etc..
    """

    penalty_type: str = field(
        default=None,
        metadata=dict(
            name="PenaltyType",
            type="Attribute",
            help=None,
        )
    )
    departure_status: str = field(
        default=None,
        metadata=dict(
            name="DepartureStatus",
            type="Attribute",
            help=None,
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
        )
    )
    percent: float = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Attribute",
            help=None,
        )
    )
    more_rules_present: bool = field(
        default=None,
        metadata=dict(
            name="MoreRulesPresent",
            type="Attribute",
            help="If true, specifies that advance purchase information will be present in fare rules.",
        )
    )


@dataclass
class Rules:
    rules_text: str = field(
        default=None,
        metadata=dict(
            name="RulesText",
            type="Element",
            help="Rules text",
        )
    )


@dataclass
class SearchTraveler(TypePassengerType):
    air_seat_assignment: List[AirSeatAssignment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSeatAssignment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class SeatInformation:
    """
    Additional information about seats. Providers: 1G, 1V, 1P, 1J,ACH
    """

    power: str = field(
        default=None,
        metadata=dict(
            name="Power",
            type="Element",
            help="Detail about any electrical power the seat might have. For example: No Power Providers: 1G, 1V, 1P, 1J",
            required=True
        )
    )
    video: str = field(
        default=None,
        metadata=dict(
            name="Video",
            type="Element",
            help="Detail about any video components the seat might have. For example: No Video Providers: 1G, 1V, 1P, 1J",
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Element",
            help="Detail about the type of seat. For example: Exit Row, Standard, etc. Providers: 1G, 1V, 1P, 1J",
            required=True
        )
    )
    description: str = field(
        default=None,
        metadata=dict(
            name="Description",
            type="Element",
            help="Detailed description of the seat. Providers: 1G, 1V, 1P, 1J",
            required=True
        )
    )
    rating: "SeatInformation.Rating" = field(
        default=None,
        metadata=dict(
            name="Rating",
            type="Element",
            help="Definition of the seat rating. Providers: 1G, 1V, 1P, 1J",
            required=True
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )

    @dataclass
    class Rating(str):
        number: int = field(
            default=None,
            metadata=dict(
                name="Number",
                type="Attribute",
                help="Numerical rating of the seat from 1 to 5 with 1 being bad and 5 being good. Providers: 1G, 1V, 1P, 1J",
                required=True
            )
        )


@dataclass
class SegmentIndex(int):
    """
    Identifies the segment that is part of this group
    """

    pass


@dataclass
class ServiceSubGroup:
    """
    The Service Sub Group of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH
    """

    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The Service Sub Group Code of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        )
    )


@dataclass
class SpecificSeatAssignment:
    """
    Request object used to specify a specific seat
    """

    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="The passenger that this seat assignment is for",
            required=True
        )
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="The segment that we will assign this seat on",
            required=True
        )
    )
    flight_detail_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="FlightDetailRef",
            type="Attribute",
            help="The Flight Detail ref of the AirSegment used when requesting seats on Change of Guage flights",
        )
    )
    seat_id: str = field(
        default=None,
        metadata=dict(
            name="SeatId",
            type="Attribute",
            help="The actual seat ID that is being requested. Special Characters are not supported in this field.",
            required=True
        )
    )
    rail_coach_number: str = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute",
            help="Coach number for which rail seatmap/coachmap is returned.",
            max_length=4.0
        )
    )


@dataclass
class SpecificTimeTable:
    flight_origin: "SpecificTimeTable.FlightOrigin" = field(
        default=None,
        metadata=dict(
            name="FlightOrigin",
            type="Element",
            help=None,
        )
    )
    flight_destination: "SpecificTimeTable.FlightDestination" = field(
        default=None,
        metadata=dict(
            name="FlightDestination",
            type="Element",
            help=None,
        )
    )
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help=None,
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
            required=True
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help=None,
            required=True
        )
    )

    @dataclass
    class FlightOrigin:
        airport: Airport = field(
            default=None,
            metadata=dict(
                name="Airport",
                type="Element",
                help=None,
                required=True
            )
        )

    @dataclass
    class FlightDestination:
        airport: Airport = field(
            default=None,
            metadata=dict(
                name="Airport",
                type="Element",
                help=None,
                required=True
            )
        )


@dataclass
class SplitTicketingSearch:
    """
    SplitTicketingSearch is optional. Used to return both One-Way and Roundtrip fares in a single search response. Applicable to 1G, 1V, 1P only, the price points results path, and a simple roundtrip search only. Cannot be used in combination with Flex options.
    """

    round_trip: int = field(
        default=None,
        metadata=dict(
            name="RoundTrip",
            type="Attribute",
            help="Percentage of Roundtrip price points to be returned in the search response. This should be an even number. The One-Way price points returned in the response would be evenly distributed between the outbound and the inbound.",
        )
    )


@dataclass
class SponsoredFltInfo:
    """
    This describes whether the segment is determined to be a sponsored flight. The SponsoredFltInfo node will only come back for Travelport UIs and not for other customers.
    """

    sponsored_lnb: int = field(
        default=None,
        metadata=dict(
            name="SponsoredLNB",
            type="Attribute",
            help="The line number of the sponsored flight item",
            required=True
        )
    )
    neutral_lnb: int = field(
        default=None,
        metadata=dict(
            name="NeutralLNB",
            type="Attribute",
            help="The neutral line number for the flight item.",
            required=True
        )
    )
    flt_key: str = field(
        default=None,
        metadata=dict(
            name="FltKey",
            type="Attribute",
            help="The unique identifying key for the sponsored flight.",
            required=True,
            max_length=5.0
        )
    )


@dataclass
class Tax:
    """
    Taxes for Land Charges
    """

    category: str = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="The tax category represents a valid IATA tax code.",
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TaxInfo(TypeTaxInfo):
    """
    The tax information for a
    """

    pass


@dataclass
class TextInfo:
    """
    Information on baggage as published by carrier.
    """

    text: List[TypeGeneralText] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    title: str = field(
        default=None,
        metadata=dict(
            name="Title",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class TicketAgency:
    """
    This modifier will override the pseudo of the ticketing agency found in the AAT (TKAG). Used for all plating carrier validation.
    """

    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The code of the Provider (e.g. 1G, 1P)",
            required=True
        )
    )
    pseudo_city_code: str = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="The PCC of the host system.",
            required=True
        )
    )


@dataclass
class TicketEndorsement:
    value: TypeEndorsement = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TicketValidity:
    """
    To be used to pass the selected segment
    """

    not_valid_before: str = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute",
            help="Fare not valid before this date.",
        )
    )
    not_valid_after: str = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute",
            help="Fare not valid after this date.",
        )
    )


@dataclass
class TicketingModifiersRef:
    """
    Reference to a shared list of Ticketing Modifers
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TravelArranger(str):
    """
    Details of Travel Arranger
    """

    company_short_name: str = field(
        default=None,
        metadata=dict(
            name="CompanyShortName",
            type="Attribute",
            help="Company Name",
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="IATA Code for Arranger",
        )
    )


@dataclass
class TypeAlliance:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeAnchorFlightData:
    """
    To support Anchor flight search contain the anchor flight details. Supported providers 1P, 1J
    """

    airline_code: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="AirlineCode",
            type="Attribute",
            help="Indicates Anchor flight carrier code",
            required=True
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="Indicates Anchor flight number",
            required=True
        )
    )
    connection_indicator: bool = field(
        default=None,
        metadata=dict(
            name="ConnectionIndicator",
            type="Attribute",
            help="Indicates that the Anchor flight has any connecting flight or not",
        )
    )


@dataclass
class TypeApplicableSegment:
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    air_itinerary_details_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirItineraryDetailsRef",
            type="Attribute",
            help=None,
        )
    )
    booking_counts: str = field(
        default=None,
        metadata=dict(
            name="BookingCounts",
            type="Attribute",
            help="Classes of service and their counts.",
        )
    )


@dataclass
class TypeAssessIndicator:
    """
    The type of AssessIndicator
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeAtpcoglobalIndicator:
    """
    Enumeration of ATPCO global indicators
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeAvailabilitySource:
    """
    Availability Source value for Sell.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=1.0
        )
    )


@dataclass
class TypeBackOffice:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeBillingDetailsDataType:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeBillingDetailsName:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeBooking:
    """
    Type of booking
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeBrandId:
    """
    The unique identifier of the brand
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=19.0
        )
    )


@dataclass
class TypeBulkTicketModifierType:
    """
    Bulk ticketing modifier type.
    """

    suppress_on_fare_calc: bool = field(
        default=None,
        metadata=dict(
            name="SuppressOnFareCalc",
            type="Attribute",
            help="Optional attribute to allow a modifier impact such as Bulk Ticketing to have information suppressed on the Fare Calc when generating supporting documents Check the specific host system which may or may not support this function",
        )
    )


@dataclass
class TypeCarCode:
    """
    Car code value. Maximum 15 characters. Applicable provider is 1G and 1V
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=15.0
        )
    )


@dataclass
class TypeCarrierCode:
    """
    Defines the type of booking codes (Primary or Secondary)
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeConnectionIndicator:
    """
    Types of connection indicator : AvailabilityAndPricing : Specified availability and pricing connection; TurnAround : Specified turn around; Stopover : Specified stopover;
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeCouponStatus:
    """
    ATA/IATA Standard coupon status.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            length=1
        )
    )


@dataclass
class TypeDaysOfOperation(AttrDow):
    pass


@dataclass
class TypeDestinationCode:
    """
    List of valid Destination Codes.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeDisplayCategory:
    """
    Type of booking
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeDiversity:
    """
    Used in Low Fare Search to better promote unique results
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeEmdnumber:
    """
    13 character EMD number
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            length=13
        )
    )


@dataclass
class TypeEquipment:
    """
    3 Letter equipment code (sometimes vary by carrier)
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            length=3
        )
    )


@dataclass
class TypeEticketability:
    """
    Defines the ability to eticket an entity (Yes, No, Required, Ticketless)
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFacility:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFailureInfo:
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    message: str = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeFareBreak:
    """
    Types of fare break.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareDirectionality:
    """
    A fare's directionality (e.g. one-way, return )
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareDiscount:
    """
    Fare Discount Calculation Method
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareGuarantee:
    """
    The status of a fare
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFarePenalty:
    """
    Penalty applicable on a Fare for change/ cancellation etc- expressed in both Money and Percentage.
    """

    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Element",
            help="The penalty (if any) - expressed as the actual amount of money. Both Amount and Percentage can be present.",
        )
    )
    percentage: TypePercentageWithDecimal = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Element",
            help="The penalty (if any) - expressed in percentage. Both Amount and Percentage can be present.",
        )
    )
    penalty_applies: str = field(
        default=None,
        metadata=dict(
            name="PenaltyApplies",
            type="Attribute",
            help=None,
        )
    )
    no_show: bool = field(
        default=None,
        metadata=dict(
            name="NoShow",
            type="Attribute",
            help="The No Show penalty (if any) to change/cancel the fare.",
        )
    )


@dataclass
class TypeFareRestrictionType:
    """
    The type of fare restriction
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareRuleCategoryCode:
    """
    Kestrel Long Fare Rule Category Codes
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareRuleFailureInfoReason:
    """
    Reason codes for Fare rule failure. Following values will be supported. MinimumStayFailure, AdvPurchaseFailure, PICTypeFailure [Passenger Identification Code Failure], StopoverTransferFailure, DateSeasonalityFailure, RoutingFailure, MileageFailure, DayTimeFailure, OpenJawUsageFailure, IndirectTravelProvision, SalesRestrictionNotMet, FICNAFare, HIFFailure [Higher Intermediate Fare/Point or Mileage Exceptions failures], IntlSurfaceSector, CurrencyUsageFailure, DiscountApplFailure, FootNoteFailure, DayTimeApplCatNotMet, DayTimeApplCatIncomplete, SeasonalityCatNotMet, SeasonalityCatIncomplete, FlightApplCatNotMet, FlightApplCatIncomplete, AdvResvAdvTicketCatNotMet, AdvResvAdvTicketCatIncomplete, BookingClassFailure, MinStayCatNotMet, MinStayCatIncomplete, StopoverCatNotMet, StopoverCatIncomplete, PermittedCombinationCatNotMet, PermittedCombinationCatNotIncomplete, BlackoutCatNotMet, BlackoutCatNotIncomplete, AccomTvlReqCatNotMet, AccomTvlReqCatIncomplete, SalesRestCatNotMet, SalesRestCatIncomplete, EligibilityCatNotMet, EligibilityCatIncomplete, TransfersCatNotMet, TransfersCatIncomplete, TransfersRoutingFailure, HIPMileageCatNotMet [Higher Intermediate Point or Mileage Exception categories not met], HIPMileageCatIncomplete [Higher Intermediate Point or Mileage Exceptions categories incomplete], ChildDiscountCatNotMet, ChildDiscountCatIncomplete, TourConductorDiscCatNotMet, TourConductorDiscCatIncomplete, AgentDiscountCatNotMet, AgentDiscountCatIncomplete, OtherDiscountCatNotMet, OtherDiscountCatIncomplete, MiscFareTagCatNotMet, MiscFareTagCatIncomplete, FareByRuleCatNotMet, FareByRuleCatIncomplete, VisitCountryCatNotMet, VisitCountryCatIncomplete, NegFaresCatNotMet, NegFaresCatIncomplete, OthFailurePTCFailed, OthFailureRecFailed, CombineabilityFailure, TravelRestrictionNotMet, SurchargesNotMet, MaximumStayFailure, FareUsageFailure, IATAFareNotValid, RecordOneFailure, Cat01EligibilityFailure, FlightApplicationsFailure, FootNoteFailure, Cat11BlackOutfailure, Cat13AccompaniedTravelRequirementFailure, Cat19ChildDiscountFailure, Cat20TourDiscountFailure, Cat21AgentDiscountApplicationFail, YYSuppressionTableFailure, HostUseOnly87, HostUseOnly88, HostUseOnly89, HostUseOnly90, HostUseOnly99, HostUseOnly100, HostUseOnly105, HostUseOnly108, HostUseOnly111, HostUseOnly112, HostUseOnly113, HostUseOnly114, HostUseOnly121, HostUseOnly122, SpareForFutureIndicators, YYSuppressionTableFailed, HIPCheckFailed, TourCodeFail, AbonnmentFareFailure, FailedSurfaceSector, IndirectTravelFailed, FailedCurrencyUsage, CAT12NotMet
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareRuleType:
    """
    The valid rule types
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareSearchOption:
    """
    Fare Search option indicator.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareStatusCode:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareTripType:
    """
    RoundTheWorld -- round the world fare
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFareTypeCode:
    """
    ATPCO fare type code (e.g. XPN)
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=5.0
        )
    )


@dataclass
class TypeFaresIndicator:
    """
    Defines the type of fares to return (Only public fares, Only private fares, Only agency private fares, Only airline private fares or all fares)
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeFeeApplication:
    """
    The type of FeeApplication
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeIgnoreStopOver:
    """
    The stop over inluded to quote fare.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeInventoryRequest:
    """
    The valid inventory types are Seamless - A, DirectAccess - B, Basic - C
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeItinerary:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeItineraryOption:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeLowFareSearchId:
    """
    Low Fare Search Id
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeMaxJourneyTime:
    """
    Maximum Journey Time for this leg (in hours) 0-99.
    """

    value: int = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_inclusive=0.0,
            max_inclusive=99.0
        )
    )


@dataclass
class TypeMealService:
    """
    Available Meal Service
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeMileOrRouteBasedFare:
    """
    Whether the fare is Mile or Route based
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeNativeSearchModifier(str):
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="The host for which the NativeModfier being added to",
            required=True
        )
    )


@dataclass
class TypeNonAirReservationRef:
    locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="LocatorCode",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeNumberOfPassengers:
    value: int = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeOverrideOption:
    """
    Below mentioned values are only supported in schema. "SuppressItineraryInvoicePrinting" - Suppress sending itinerary/invoice document to a printer. The itinerary/invoice can be sent to a printer at a future time using duplicate itinerary/invoice. This is used by Worldspan. "PrintTerminalCodes" - Produces an itinerary/invoice or pocket itinerary that includes departure and /or arrival terminal codes. This is used by Worldspan. "PrintDirectAccessRecordLocator" - Print record locator for direct access carriers. This option prints the record locator below the segmnet information. This option can be used along with PrintProviderReservationRecordLocator as well. This is used by Worldspan. "PrintProviderReservationRecordLocator" - Print PNR record locator on documents. This option can be used along with PrintDirectAccessRecordLocator as well. This is used by Worldspan. "ReIssueTicketedStoredFare" - This modifier is used to issue a ticket against a ticket record that was previously issued. This is used by Worldspan. "PrintFrequentTravelerNumber" - This modifier is used to print frequent traveller number. This is used by Worldspan. "SuppressInvoiceNumberPrinting" - This modifier prevents the invoice number from printing on documents. This is used by Worldspan. "PrintItineraryInvoicePerTraveler" - Issues itinerary/invoice for per traveler. This is used by Worldspan. "PrintItineraryInvoicePerSurname" - Issues itinerary/invoice for per surname. This is used by Worldspan. "PrintMultipleCustomizedNameData" - Prints names individually with associated customized name data on documents. This is used by Worldspan. "PrintInvoiceRemarkOnly" - Prints invoice remark only. overrides the system remarks and directs only specific remarks selected to print on documents. This is used by Worldspan. "PrintItineraryRemarkOnly" - Prints itinerary remark only. This is used by Worldspan. "PrintBaggageAllowance" - Print the baggage allowance field with the autoprice or stored in the ticket record on credit memos/pocket Itineraries or itinerary invoices issued in conjunction with a non electronic ticket. This is used by Worldspan.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=50.0
        )
    )


@dataclass
class TypePassengerTicketNumber:
    """
    Reference Ticket Number
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=1.0,
            max_length=13.0
        )
    )


@dataclass
class TypePosition:
    """
    Facility position with respect to position within the aircraft cabin. Possible values are – Left, Right, Center, Left Center, Right Center
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypePricingMethod:
    """
    The method at which the pricing data was acquired
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypePrivateFare:
    """
    List the types of private fares, Agency private fare, Airline private Fare and Unknown. Also, this enumaration list includes PrivateFare to indetify private fares for GDSs where we can not identify specific private fares.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypePurposeCode:
    """
    List of valid Purpose Codes.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeRefundabilityValue:
    """
    Currently returned: FullyRefundable (1G,1V), RefundableWithPenalty (1G,1V), Refundable (1P,1J), NonRefundable (1G,1V,1P,1J).
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeReportingType:
    """
    The valid reporting types
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeRowLocation:
    """
    Facility Position with respect to a Row. Possible values are Rear, Front
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeSeatAvailability:
    """
    Seat availability info of a seat map
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeSegmentRef:
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeStayUnit:
    """
    Units for the Length of Stay
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeSubCode:
    """
    Used to specify an OB fee as exempt.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeTcrnumber:
    """
    The identifying number for a Ticketless Air Reservation
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeTcrstatus:
    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeTextElement(str):
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
            required=True
        )
    )
    language_code: str = field(
        default=None,
        metadata=dict(
            name="LanguageCode",
            type="Attribute",
            help="ISO 639 two-character language codes are used to retrieve specific information in the requested language. For Rich Content and Branding, language codes ZH-HANT (Chinese Traditional), ZH-HANS (Chinese Simplified), FR-CA (French Canadian) and PT-BR (Portuguese Brazil) can also be used. For RCH, language codes ENGB, ENUS, DEDE, DECH can also be used. Only certain services support this attribute. Providers: ACH, RCH, 1G, 1V, 1P, 1J.",
        )
    )


@dataclass
class TypeTicketDesignator:
    """
    Ticket Designator type.Size can be up to 20 characters
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            min_length=0.0,
            max_length=20.0
        )
    )


@dataclass
class TypeTicketModifierAccountingType:
    """
    Ticketing Modifier used to add accounting - discount information.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class TypeTicketModifierAmountType:
    """
    Ticketing Modifier used to alter a fare amount before or during the ticketing operation.
    """

    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="Amount associated with a ticketing modifier",
            required=True
        )
    )


@dataclass
class TypeTicketModifierPercentType:
    """
    Ticketing Modifier used to alter a fare percentage before or during the ticketing operation.
    """

    percent: TypePercentageWithDecimal = field(
        default=None,
        metadata=dict(
            name="Percent",
            type="Attribute",
            help="Percent associated with a ticketing modifier",
            required=True
        )
    )


@dataclass
class TypeTicketModifierValueType:
    """
    Ticketing Modifier used to add value discount information.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Element",
            help=None,
            required=True
        )
    )
    net_fare_value: bool = field(
        default=None,
        metadata=dict(
            name="NetFareValue",
            type="Attribute",
            help="Treat the value as net fare discount information",
        )
    )


@dataclass
class TypeTourCode:
    """
    Tour code value. Maximum 15 characters
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=15.0
        )
    )


@dataclass
class TypeTripType:
    """
    Used in Low Fare Search to better target the results
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeUnitOfMeasure:
    value: float = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
        )
    )
    unit: str = field(
        default=None,
        metadata=dict(
            name="Unit",
            type="Attribute",
            help="Unit values would be lb,Lb,kg etc.",
        )
    )


@dataclass
class TypeUnitWeight:
    """
    The available units of weight
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeValueCode:
    """
    Value code value. Maximum 15 characters. Applicable provider is 1G and 1V
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
            max_length=15.0
        )
    )


@dataclass
class TypeVarianceIndicator:
    """
    Type code for Variance.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class TypeVarianceType:
    """
    Type code for Variance.
    """

    value: str = field(
        default=None,
        metadata=dict(
            name="value",
            type="Restriction",
            help=None,
        )
    )


@dataclass
class UpsellBrand:
    """
    Upsell brand reference
    """

    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help=None,
        )
    )
    fare_info_ref: str = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Url(str):
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Urlinfo:
    """
    Contains the text and URL of baggage as published by carrier.
    """

    text: List[TypeGeneralText] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    url: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="URL",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class ValueDetails:
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help=None,
            required=True
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class VoidDocumentInfo(AttrDocument):
    """
    Container to represent document information.
    """

    pass


@dataclass
class VoidFailureInfo(str):
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help=None,
            required=True
        )
    )
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class VoidResultInfo(AttrDocument):
    """
    List of Successful Or Failed void document results.
    """

    failure_remark: str = field(
        default=None,
        metadata=dict(
            name="FailureRemark",
            type="Element",
            help="Container to show all provider failure information.",
        )
    )
    result_type: str = field(
        default=None,
        metadata=dict(
            name="ResultType",
            type="Attribute",
            help="Successful Or Failed result indicator.",
        )
    )


@dataclass
class Yield:
    """
    An identifier which identifies yield made on original pricing. It can be a flat amount of original price. The value of Amount can be negative. Negative value implies a discount.
    """

    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help="Yield per passenger level in Default Currency for this entity.",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Reference to a booking traveler for which Yield is applied.",
        )
    )


@dataclass
class Affiliations:
    """
    Affiliations related for pre pay profiles
    """

    travel_arranger: List[TravelArranger] = field(
        default_factory=list,
        metadata=dict(
            name="TravelArranger",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirAvailInfo:
    """
    Matches class of service information with availability counts. Only provided on search results.
    """

    booking_code_info: List[BookingCodeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCodeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_token_info: List["AirAvailInfo.FareTokenInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="FareTokenInfo",
            type="Element",
            help="Associates Fare with HostToken",
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
        )
    )
    host_token_ref: str = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute",
            help=None,
        )
    )

    @dataclass
    class FareTokenInfo:
        fare_info_ref: str = field(
            default=None,
            metadata=dict(
                name="FareInfoRef",
                type="Attribute",
                help=None,
                required=True
            )
        )
        host_token_ref: str = field(
            default=None,
            metadata=dict(
                name="HostTokenRef",
                type="Attribute",
                help=None,
                required=True
            )
        )


@dataclass
class AirExchangeBundle:
    """
    Used both in request and response
    """

    air_exchange_info: AirExchangeInfo = field(
        default=None,
        metadata=dict(
            name="AirExchangeInfo",
            type="Element",
            help=None,
            required=True
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    penalty: List[Penalty] = field(
        default_factory=list,
        metadata=dict(
            name="Penalty",
            type="Element",
            help="Only used within an AirExchangeQuoteRsp",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeBundleTotal:
    """
    Total exchange and penalty information for one ticket number
    """

    air_exchange_info: AirExchangeInfo = field(
        default=None,
        metadata=dict(
            name="AirExchangeInfo",
            type="Element",
            help=None,
            required=True
        )
    )
    penalty: List[Penalty] = field(
        default_factory=list,
        metadata=dict(
            name="Penalty",
            type="Element",
            help="Only used within an AirExchangeQuoteRsp",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeModifiers:
    """
    Provides controls and switches for the Exchange process
    """

    contract_codes: "AirExchangeModifiers.ContractCodes" = field(
        default=None,
        metadata=dict(
            name="ContractCodes",
            type="Element",
            help=None,
        )
    )
    booking_date: str = field(
        default=None,
        metadata=dict(
            name="BookingDate",
            type="Attribute",
            help=None,
        )
    )
    ticketing_date: str = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute",
            help=None,
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help=None,
        )
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            help=None,
        )
    )
    allow_penalty_fares: bool = field(
        default="true",
        metadata=dict(
            name="AllowPenaltyFares",
            type="Attribute",
            help=None,
        )
    )
    private_fares_only: bool = field(
        default="false",
        metadata=dict(
            name="PrivateFaresOnly",
            type="Attribute",
            help=None,
        )
    )
    universal_record_locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="UniversalRecordLocatorCode",
            type="Attribute",
            help="Which UniversalRecord should this new reservation be applied to. If blank, then a new one is created.",
        )
    )
    provider_locator_code: TypeLocatorCode = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Which Provider reservation does this reservation get added to.",
        )
    )
    provider_code: str = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="To be used with ProviderLocatorCode, which host the reservation being added to belongs to.",
        )
    )

    @dataclass
    class ContractCodes:
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata=dict(
                name="ContractCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirFareDiscount:
    """
    Fare Discounts
    """

    percentage: float = field(
        default=None,
        metadata=dict(
            name="Percentage",
            type="Attribute",
            help=None,
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
        )
    )
    discount_method: TypeFareDiscount = field(
        default=None,
        metadata=dict(
            name="DiscountMethod",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirFareRuleCategory:
    """
    A collection of fare rule category codes.
    """

    category_code: List[TypeFareRuleCategoryCode] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryCode",
            type="Element",
            help="The Category Code for Air Fare Rule.",
            min_occurs=1,
            max_occurs=10
        )
    )
    fare_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirPricingAdjustment:
    """
    This is a container to adjust price of AirPricingInfo. Pass zero values to remove existing adjustment.
    """

    adjustment: Adjustment = field(
        default=None,
        metadata=dict(
            name="Adjustment",
            type="Element",
            help=None,
            required=True
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Key of AirPricingInfo from booking.",
            required=True
        )
    )


@dataclass
class AirPricingPayment:
    """
    AirPricing Payment information - used to associate a FormOfPayment withiin the UR with one or more AirPricingInfos
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirRefundModifiers:
    """
    Provides controls and switches for the Refund process
    """

    refund_date: str = field(
        default=None,
        metadata=dict(
            name="RefundDate",
            type="Attribute",
            help=None,
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help=None,
        )
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirSegmentDetails:
    """
    An Air marketable travel segment.
    """

    passenger_details_ref: List[PassengerDetailsRef] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerDetailsRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    brand_id: List[BrandId] = field(
        default_factory=list,
        metadata=dict(
            name="BrandID",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    booking_code_list: str = field(
        default=None,
        metadata=dict(
            name="BookingCodeList",
            type="Element",
            help="Lists classes of service and their counts separated by delimiter |.",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help=None,
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
            required=True
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
            required=True
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
            required=True
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help="The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    equipment: TypeEquipment = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            help=None,
        )
    )
    class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            help=None,
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help=None,
        )
    )
    operating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="OperatingCarrier",
            type="Attribute",
            help="The actual carrier that is operating the flight.",
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="Flight Number for the Search Leg Detail.",
            required=True
        )
    )


@dataclass
class AirSegmentPricingModifiers:
    """
    Specifies modifiers that a particular segment should be priced in. If this is used, then there must be one for each AirSegment in the AirItinerary.
    """

    permitted_booking_codes: "AirSegmentPricingModifiers.PermittedBookingCodes" = field(
        default=None,
        metadata=dict(
            name="PermittedBookingCodes",
            type="Element",
            help=None,
        )
    )
    air_segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Attribute",
            help=None,
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help=None,
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help=None,
        )
    )
    prohibit_advance_purchase_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitAdvancePurchaseFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_penalty_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitPenaltyFares",
            type="Attribute",
            help=None,
        )
    )
    fare_basis_code: str = field(
        default=None,
        metadata=dict(
            name="FareBasisCode",
            type="Attribute",
            help="The fare basis code to be used for pricing.",
        )
    )
    fare_break: TypeFareBreak = field(
        default=None,
        metadata=dict(
            name="FareBreak",
            type="Attribute",
            help="Fare break point modifier to instruct Fares where it should or should not break the fare.",
        )
    )
    connection_indicator: TypeConnectionIndicator = field(
        default=None,
        metadata=dict(
            name="ConnectionIndicator",
            type="Attribute",
            help="ConnectionIndicator attribute will be used to map connection indicators AvailabilityAndPricing, TurnAround and Stopover. This attribute is for Wordspan/1P only.",
        )
    )
    brand_tier: StringLength1to10 = field(
        default=None,
        metadata=dict(
            name="BrandTier",
            type="Attribute",
            help="Modifier to price by specific brand tier number.",
        )
    )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AlternateLocationDistanceList:
    """
    Provides the Distance Information between Original Search Airports or City to Alternate Search Airports
    """

    alternate_location_distance: List[AlternateLocationDistance] = field(
        default_factory=list,
        metadata=dict(
            name="AlternateLocationDistance",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class Apisrequirements:
    """
    Specific details for APIS Requirements.
    """

    document: List[Document] = field(
        default_factory=list,
        metadata=dict(
            name="Document",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: str = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Unique identifier for this APIS Requirements - use this key when a single APIS Requirements is shared by multiple elements.",
        )
    )
    level: str = field(
        default=None,
        metadata=dict(
            name="Level",
            type="Attribute",
            help="Applicability level of the Document. Required, Supported, API_Supported or Unknown",
        )
    )
    gender_required: bool = field(
        default=None,
        metadata=dict(
            name="GenderRequired",
            type="Attribute",
            help=None,
        )
    )
    date_of_birth_required: bool = field(
        default=None,
        metadata=dict(
            name="DateOfBirthRequired",
            type="Attribute",
            help=None,
        )
    )
    required_documents: str = field(
        default=None,
        metadata=dict(
            name="RequiredDocuments",
            type="Attribute",
            help="What are required documents for the APIS Requirement. One, FirstAndOneOther or All",
        )
    )
    nationality_required: bool = field(
        default=None,
        metadata=dict(
            name="NationalityRequired",
            type="Attribute",
            help="Nationality of the traveler is required for booking for some suppliers.",
        )
    )


@dataclass
class ApplicableSegment(TypeApplicableSegment):
    """
    Applicable air segment.
    """

    pass


@dataclass
class AttrEmdsummary:
    """
    Details of Booking Traveler Name
    """

    number: TypeEmdnumber = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help="EMD Number",
            required=True
        )
    )
    primary_document_indicator: bool = field(
        default=None,
        metadata=dict(
            name="PrimaryDocumentIndicator",
            type="Attribute",
            help="Indicates whether the EMD is a primary EMD.",
        )
    )
    in_conjunction_with: TypeEmdnumber = field(
        default=None,
        metadata=dict(
            name="InConjunctionWith",
            type="Attribute",
            help="Returns the number of the Primary EMD, if this EMD is a conjunctive EMD",
        )
    )
    associated_ticket_number: TypeTicketNumber = field(
        default=None,
        metadata=dict(
            name="AssociatedTicketNumber",
            type="Attribute",
            help="This number indicates the e-Ticket number associated with this EMD",
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="Plating carrier code for which this EMD is issued",
        )
    )
    issue_date: str = field(
        default=None,
        metadata=dict(
            name="IssueDate",
            type="Attribute",
            help="Issue Date for this EMD",
        )
    )


@dataclass
class AuditData(AttrPrices):
    """
    Container for Pricing Audit Data.For providers 1P/1J
    """

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class BackOfficeHandOff:
    """
    Allows an agency to select the back office documents and also route to different host to produce for the itinerary.
    """

    type: TypeBackOffice = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The type of back office document,valid options are Accounting,Global,NonAccounting,NonAccountingRemote,Dual.",
            required=True
        )
    )
    location: str = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute",
            help="This is required for NonAccountingRemote,Dual and Global type back office.",
        )
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="The PCC of the host system where it would be routed.",
        )
    )


@dataclass
class BaseBaggageAllowanceInfo:
    """
    This contains common elements that are used for Baggage Allowance info, carry-on allowance info and embargo Info. Supported providers are 1V/1G/1P/1J
    """

    urlinfo: List[Urlinfo] = field(
        default_factory=list,
        metadata=dict(
            name="URLInfo",
            type="Element",
            help="Contains the text and URL information as published by carrier.",
            min_occurs=0,
            max_occurs=999
        )
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TextInfo",
            type="Element",
            help="Text information as published by carrier.",
            min_occurs=0,
            max_occurs=999
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help=None,
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help=None,
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class BillingDetailItem:
    """
    The Billing Details Information
    """

    name: TypeBillingDetailsName = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="Detailed Billing Information Name(e.g Personal ID, Account Number)",
            required=True
        )
    )
    data_type: TypeBillingDetailsDataType = field(
        default=None,
        metadata=dict(
            name="DataType",
            type="Attribute",
            help="Detailed Billing Information DataType (Alpha, Numeric, etc.)",
            required=True
        )
    )
    min_length: str = field(
        default=None,
        metadata=dict(
            name="MinLength",
            type="Attribute",
            help="Detailed Billing Information Minimum Length.",
            required=True
        )
    )
    max_length: str = field(
        default=None,
        metadata=dict(
            name="MaxLength",
            type="Attribute",
            help="Detailed Billing Information Maximum Length.",
            required=True
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help="Detailed Billing Information Value",
        )
    )


@dataclass
class BookingRulesFareReference(str):
    """
    Fare Reference associated with the BookingRules. Containing a text container for vendor response text.
    """

    class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            help=None,
        )
    )
    ticket_designator_code: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="TicketDesignatorCode",
            type="Attribute",
            help=None,
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help=None,
        )
    )
    upgrage_allowed: bool = field(
        default=None,
        metadata=dict(
            name="UpgrageAllowed",
            type="Attribute",
            help=None,
        )
    )
    upgrade_class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="UpgradeClassOfService",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class BrandInfo:
    """
    Commercially recognized product offered by an airline
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Brand Key",
        )
    )
    brand_id: TypeBrandId = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            help="The unique identifier of the brand",
            required=True
        )
    )
    air_pricing_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Attribute",
            help="A reference to a AirPricing. Providers: ACH, 1G, 1V, 1P, 1J.",
        )
    )
    fare_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help="A reference to a FareInfo. Providers: ACH, 1G, 1V, 1P, 1J.",
        )
    )


@dataclass
class BundledService:
    """
    Displays the services bundled together
    """

    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="Carrier the service is applicable.",
        )
    )
    carrier_sub_code: bool = field(
        default=None,
        metadata=dict(
            name="CarrierSubCode",
            type="Attribute",
            help="Carrier sub code. True means the carrier used their own sub code. False means the carrier used an ATPCO sub code",
        )
    )
    service_type: str = field(
        default=None,
        metadata=dict(
            name="ServiceType",
            type="Attribute",
            help="The type of service or what the service is used for, e.g. F type is flight type, meaning the service is used on a flight",
        )
    )
    service_sub_code: str = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            help="The sub code of the service, e.g. OAA for Pre paid baggage",
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="Name of the bundled service.",
        )
    )
    booking: TypeBooking = field(
        default=None,
        metadata=dict(
            name="Booking",
            type="Attribute",
            help="Booking method for the bundled service, e..g SSR.",
        )
    )
    occurrence: int = field(
        default=None,
        metadata=dict(
            name="Occurrence",
            type="Attribute",
            help="How many of the service are included in the bundled service.",
        )
    )


@dataclass
class CarrierList:
    carrier_code: List[CarrierCode] = field(
        default_factory=list,
        metadata=dict(
            name="CarrierCode",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=6
        )
    )
    include_carrier: bool = field(
        default=None,
        metadata=dict(
            name="IncludeCarrier",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class CategoryDetailsType:
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryDetails",
            type="Element",
            help="For each category Details of Structured Fare Rules",
            min_occurs=0,
            max_occurs=99
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class Characteristic:
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )
    position: TypePosition = field(
        default=None,
        metadata=dict(
            name="Position",
            type="Attribute",
            help=None,
        )
    )
    row_location: TypeRowLocation = field(
        default=None,
        metadata=dict(
            name="RowLocation",
            type="Attribute",
            help=None,
        )
    )
    padiscode: StringLength1to99 = field(
        default=None,
        metadata=dict(
            name="PADISCode",
            type="Attribute",
            help="Industry standard code that defines seat and row characteristic.",
        )
    )


@dataclass
class ChargesRules:
    """
    Fare Reference associated with the BookingRules
    """

    voluntary_changes: List["ChargesRules.VoluntaryChanges"] = field(
        default_factory=list,
        metadata=dict(
            name="VoluntaryChanges",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    voluntary_refunds: List["ChargesRules.VoluntaryRefunds"] = field(
        default_factory=list,
        metadata=dict(
            name="VoluntaryRefunds",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class VoluntaryChanges:
        penalty: Penalty = field(
            default=None,
            metadata=dict(
                name="Penalty",
                type="Element",
                help=None,
            )
        )
        vol_change_ind: bool = field(
            default=None,
            metadata=dict(
                name="VolChangeInd",
                type="Attribute",
                help=None,
            )
        )

    @dataclass
    class VoluntaryRefunds:
        penalty: Penalty = field(
            default=None,
            metadata=dict(
                name="Penalty",
                type="Element",
                help=None,
            )
        )
        vol_change_ind: bool = field(
            default=None,
            metadata=dict(
                name="VolChangeInd",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class Chgtype:
    """
    PenFee list will be populated
    """

    pen_fee: List[PenFeeType] = field(
        default_factory=list,
        metadata=dict(
            name="PenFee",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )


@dataclass
class Co2Emissions:
    """
    The carbon emissions produced by the journey
    """

    co2_emission: List[Co2Emission] = field(
        default_factory=list,
        metadata=dict(
            name="CO2Emission",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    total_value: float = field(
        default=None,
        metadata=dict(
            name="TotalValue",
            type="Attribute",
            help="The total CO2 emission value for the journey",
        )
    )
    unit: StringLength1to64 = field(
        default=None,
        metadata=dict(
            name="Unit",
            type="Attribute",
            help="The unit used in the TotalValue attribute",
        )
    )
    category: StringLength1to64 = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help="The category name of the type of cabin, either Economy or Premium. Premium is any cabin that is not considered Economy",
        )
    )
    source: StringLength1to64 = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            help="The source responsible for the values",
        )
    )


@dataclass
class Connection:
    """
    Flight Connection Information
    """

    fare_note: FareNote = field(
        default=None,
        metadata=dict(
            name="FareNote",
            type="Element",
            help=None,
        )
    )
    change_of_plane: bool = field(
        default="false",
        metadata=dict(
            name="ChangeOfPlane",
            type="Attribute",
            help="Indicates the traveler must change planes between flights.",
        )
    )
    change_of_terminal: bool = field(
        default="false",
        metadata=dict(
            name="ChangeOfTerminal",
            type="Attribute",
            help="Indicates the traveler must change terminals between flights.",
        )
    )
    change_of_airport: bool = field(
        default="false",
        metadata=dict(
            name="ChangeOfAirport",
            type="Attribute",
            help="Indicates the traveler must change airports between flights.",
        )
    )
    stop_over: bool = field(
        default="false",
        metadata=dict(
            name="StopOver",
            type="Attribute",
            help="Indicates that there is a significant delay between flights (usually 12 hours or more)",
        )
    )
    min_connection_time: int = field(
        default=None,
        metadata=dict(
            name="MinConnectionTime",
            type="Attribute",
            help="The minimum time needed to connect between the two different destinations.",
        )
    )
    duration: int = field(
        default=None,
        metadata=dict(
            name="Duration",
            type="Attribute",
            help="The actual duration (in minutes) between flights.",
        )
    )
    segment_index: int = field(
        default=None,
        metadata=dict(
            name="SegmentIndex",
            type="Attribute",
            help="The sequential AirSegment number that this connection information applies to.",
        )
    )
    flight_details_index: int = field(
        default=None,
        metadata=dict(
            name="FlightDetailsIndex",
            type="Attribute",
            help="The sequential FlightDetails number that this connection information applies to.",
        )
    )
    include_stop_over_to_fare_quote: TypeIgnoreStopOver = field(
        default=None,
        metadata=dict(
            name="IncludeStopOverToFareQuote",
            type="Attribute",
            help="The field determines to quote fares with or without stop overs,the values can be NoStopOver,StopOver and IgnoreSegment.",
        )
    )


@dataclass
class DestinationPurposeCode:
    """
    This code is required to indicate destination and purpose of Travel. It is applicable for Canada and Bermuda agency only. This is used by Worldspan.
    """

    destination: TypeDestinationCode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help=None,
            required=True
        )
    )
    purpose: TypePurposeCode = field(
        default=None,
        metadata=dict(
            name="Purpose",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class Dimension(TypeUnitOfMeasure):
    """
    Information related to Length,Height,Width of a baggage.
    """

    type: str = field(
        default=None,
        metadata=dict(
            name="type",
            type="Attribute",
            help="Type denotes Length,Height,Width of a baggage.",
        )
    )


@dataclass
class DocumentOptions:
    """
    Allows an agency to set different document options for the itinerary.
    """

    passenger_receipt_override: PassengerReceiptOverride = field(
        default=None,
        metadata=dict(
            name="PassengerReceiptOverride",
            type="Element",
            help=None,
        )
    )
    override_option: List[TypeOverrideOption] = field(
        default_factory=list,
        metadata=dict(
            name="OverrideOption",
            type="Element",
            help="Allows an agency to override print options for documents during document generation.",
            min_occurs=0,
            max_occurs=999
        )
    )
    suppress_itinerary_remarks: bool = field(
        default=None,
        metadata=dict(
            name="SuppressItineraryRemarks",
            type="Attribute",
            help="True when itinerary remarks are suppressed.",
        )
    )
    generate_itin_numbers: bool = field(
        default=None,
        metadata=dict(
            name="GenerateItinNumbers",
            type="Attribute",
            help="True when itinerary numbers are system generated.",
        )
    )


@dataclass
class EmbargoList:
    """
    List of embargoes. Provider: 1G, 1V, 1P, 1J
    """

    embargo: List[Embargo] = field(
        default_factory=list,
        metadata=dict(
            name="Embargo",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class Emd:
    fulfillment_type: int = field(
        default=None,
        metadata=dict(
            name="FulfillmentType",
            type="Attribute",
            help="A one digit code specifying how the service must be fulfilled. See FulfillmentTypeDescription for the description of this value.",
            min_inclusive=1.0,
            max_inclusive=5.0
        )
    )
    fulfillment_type_description: str = field(
        default=None,
        metadata=dict(
            name="FulfillmentTypeDescription",
            type="Attribute",
            help="EMD description.",
        )
    )
    associated_item: str = field(
        default=None,
        metadata=dict(
            name="AssociatedItem",
            type="Attribute",
            help="The type of Optional Service. The choices are Flight, Ticket, Merchandising, Rule Buster, Allowance, Chargeable Baggage, Carry On Baggage Allowance, Prepaid Baggage. Provider: 1G, 1V, 1P, 1J",
        )
    )
    availability_charge_indicator: str = field(
        default=None,
        metadata=dict(
            name="AvailabilityChargeIndicator",
            type="Attribute",
            help="A one-letter code specifying whether the service is available or if there is a charge associated with it. X = Service not available F = No charge for service (free) and an EMD is not issued to reflect free service E = No charge for service (free) and an EMD is issued to reflect the free service. G = No charge for service (free), booking is not required and an EMD is not issued to reflect free service H = No charge for service (free), booking is not required, and an EMD is issued to reflect the free service. Blank = No application. Charges apply according to the data in the Service Fee fields.",
        )
    )
    refund_reissue_indicator: str = field(
        default=None,
        metadata=dict(
            name="RefundReissueIndicator",
            type="Attribute",
            help="An attribute specifying whether the service is refundable or reissuable.",
        )
    )
    commissionable: bool = field(
        default=None,
        metadata=dict(
            name="Commissionable",
            type="Attribute",
            help="True/False value to whether or not the service is comissionable.",
        )
    )
    mileage_indicator: bool = field(
        default=None,
        metadata=dict(
            name="MileageIndicator",
            type="Attribute",
            help="True/False value to whether or not the service has miles.",
        )
    )
    location: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Location",
            type="Attribute",
            help="3 letter location code where the service will be availed.",
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="Date",
            type="Attribute",
            help="The date at which the service will be used.",
        )
    )
    booking: TypeBooking = field(
        default=None,
        metadata=dict(
            name="Booking",
            type="Attribute",
            help="Holds the booking description for the service, e.g., SSR.",
        )
    )
    display_category: TypeDisplayCategory = field(
        default=None,
        metadata=dict(
            name="DisplayCategory",
            type="Attribute",
            help="Describes when the service should be displayed.",
        )
    )
    reusable: bool = field(
        default=None,
        metadata=dict(
            name="Reusable",
            type="Attribute",
            help="Identifies if the service can be re-used towards a future purchase.",
        )
    )


@dataclass
class EmdpricingInfo:
    """
    Fare related information for these electronic miscellaneous documents. Supported providers are 1G/1V/1P/1J
    """

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    base_fare: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute",
            help=None,
        )
    )
    total_fare: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalFare",
            type="Attribute",
            help=None,
        )
    )
    total_tax: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalTax",
            type="Attribute",
            help=None,
        )
    )
    equiv_fare: TypeMoney = field(
        default=None,
        metadata=dict(
            name="EquivFare",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class ExchangePenaltyInfo:
    penalty_information: List[PenaltyInformation] = field(
        default_factory=list,
        metadata=dict(
            name="PenaltyInformation",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ptc: TypePtc = field(
        default=None,
        metadata=dict(
            name="PTC",
            type="Attribute",
            help=None,
        )
    )
    minimum_change_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="MinimumChangeFee",
            type="Attribute",
            help="Minimum change fee for changes to the itinerary.",
        )
    )
    maximum_change_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="MaximumChangeFee",
            type="Attribute",
            help="Maximum change fee for changes to the itinerary.",
        )
    )


@dataclass
class ExemptObfee:
    """
    Used to specify which OB fees are exempt; if none are listed, it means all should be exempt.
    """

    sub_code: List[TypeSubCode] = field(
        default_factory=list,
        metadata=dict(
            name="SubCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=8
        )
    )


@dataclass
class FareGuaranteeInfo:
    """
    The information related to fare guarantee details.
    """

    guarantee_date: str = field(
        default=None,
        metadata=dict(
            name="GuaranteeDate",
            type="Attribute",
            help="The date till which the fare is guaranteed.",
        )
    )
    guarantee_type: TypeFareGuarantee = field(
        default=None,
        metadata=dict(
            name="GuaranteeType",
            type="Attribute",
            help="Determines the status of a fare for a passenger.",
            required=True
        )
    )


@dataclass
class FareNoteList:
    """
    The shared object list of Notes
    """

    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class FareRemark:
    text: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    url: List[Url] = field(
        default_factory=list,
        metadata=dict(
            name="URL",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRestrictionDate:
    """
    Fare restriction based on date ranges. StartDate and EndDate are strings representing respective dates. If a year component is present then it signifies an exact date. If only day and month components are present then it signifies a seasonal date, which means applicable for that date in any year
    """

    direction: TypeFareDirectionality = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute",
            help=None,
        )
    )
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help=None,
        )
    )
    end_date: str = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute",
            help=None,
        )
    )
    end_date_indicator: str = field(
        default=None,
        metadata=dict(
            name="EndDateIndicator",
            type="Attribute",
            help="This field indicates the end date/last date for which travel on the fare component being validated must be commenced or completed",
        )
    )


@dataclass
class FareRestrictionDaysOfWeek:
    """
    Days of the week that the restriction applies too.
    """

    direction: TypeFareDirectionality = field(
        default=None,
        metadata=dict(
            name="Direction",
            type="Attribute",
            help=None,
        )
    )
    trip_type: TypeFareTripType = field(
        default=None,
        metadata=dict(
            name="TripType",
            type="Attribute",
            help=None,
        )
    )
    monday: bool = field(
        default=None,
        metadata=dict(
            name="Monday",
            type="Attribute",
            help=None,
        )
    )
    tuesday: bool = field(
        default=None,
        metadata=dict(
            name="Tuesday",
            type="Attribute",
            help=None,
        )
    )
    wednesday: bool = field(
        default=None,
        metadata=dict(
            name="Wednesday",
            type="Attribute",
            help=None,
        )
    )
    thursday: bool = field(
        default=None,
        metadata=dict(
            name="Thursday",
            type="Attribute",
            help=None,
        )
    )
    friday: bool = field(
        default=None,
        metadata=dict(
            name="Friday",
            type="Attribute",
            help=None,
        )
    )
    saturday: bool = field(
        default=None,
        metadata=dict(
            name="Saturday",
            type="Attribute",
            help=None,
        )
    )
    sunday: bool = field(
        default=None,
        metadata=dict(
            name="Sunday",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRuleFailureInfo:
    """
    Returns fare rule failure reason codes when fare basis code is forced.
    """

    reason: List[TypeFareRuleFailureInfoReason] = field(
        default_factory=list,
        metadata=dict(
            name="Reason",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareRuleShort:
    """
    Short Text Fare Rule
    """

    fare_rule_name_value: List[FareRuleNameValue] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleNameValue",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    category: int = field(
        default=None,
        metadata=dict(
            name="Category",
            type="Attribute",
            help=None,
            required=True
        )
    )
    table_number: str = field(
        default=None,
        metadata=dict(
            name="TableNumber",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareStatus:
    """
    Denotes the status of a particular fare.
    """

    fare_status_failure_info: FareStatusFailureInfo = field(
        default=None,
        metadata=dict(
            name="FareStatusFailureInfo",
            type="Element",
            help=None,
        )
    )
    code: TypeFareStatusCode = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The status of the fare.",
            required=True
        )
    )


@dataclass
class FareTicketDesignator:
    """
    Ticket Designator used to further qualify a Fare
    """

    value: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareType:
    """
    Used to request fares based on the ATPCO type code
    """

    code: TypeFareTypeCode = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FeeApplication(TypeFeeApplication):
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The code associated to the fee application. The choices are: 1, 2, 3, 4, 5, K, F",
            length=1
        )
    )


@dataclass
class GroupedOptionInfo:
    grouped_option: List[GroupedOption] = field(
        default_factory=list,
        metadata=dict(
            name="GroupedOption",
            type="Element",
            help=None,
            min_occurs=2,
            max_occurs=999
        )
    )


@dataclass
class IncludeAddlBookingCodeInfo:
    """
    Used to include primary or secondary carrier's booking code details
    """

    type: TypeCarrierCode = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The type defines that the booking code info is for primary or secondary carrier.",
            required=True
        )
    )
    secondary_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="SecondaryCarrier",
            type="Attribute",
            help="The secondary carrier code is required when type is secondary .",
        )
    )


@dataclass
class InvoluntaryChange:
    """
    Specify the Ticket Endorsement value
    """

    ticket_endorsement: TicketEndorsement = field(
        default=None,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class IssuanceModifiers:
    """
    General modifiers supported for EMD Issuance.Supported providers are 1V/1G/1P/1J
    """

    customer_receipt_info: CustomerReceiptInfo = field(
        default=None,
        metadata=dict(
            name="CustomerReceiptInfo",
            type="Element",
            help="Information about customer receipt via email.",
        )
    )
    emdendorsement: Emdendorsement = field(
        default=None,
        metadata=dict(
            name="EMDEndorsement",
            type="Element",
            help="Endorsement details to be used during EMD issuance.",
        )
    )
    emdcommission: Emdcommission = field(
        default=None,
        metadata=dict(
            name="EMDCommission",
            type="Element",
            help="Commission information to be used for EMD issuance.",
        )
    )
    form_of_payment_ref: FormOfPaymentRef = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            help="Reference to FormOfPayment present in the UR to be used for EMD issuance.",
        )
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="FormOfPayment information to be used for EMD issuance.",
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="Plating carrier code for which this EMD is issued.",
        )
    )


@dataclass
class Itinerary:
    """
    Allows an agency to select the itinenary option for ticket.
    """

    type: TypeItinerary = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Specifies the type of itinenary option for ticket like Invoice type or Pocket itinenary.",
        )
    )
    option: TypeItineraryOption = field(
        default=None,
        metadata=dict(
            name="Option",
            type="Attribute",
            help="Specifies the itinerary option like NoFare,NoAmount.",
        )
    )
    separate_indicator: bool = field(
        default=None,
        metadata=dict(
            name="SeparateIndicator",
            type="Attribute",
            help="Set to true if one itinerary to be printed per passenger.",
        )
    )


@dataclass
class Journey:
    """
    Information about all connecting segment list and total traveling time
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    travel_time: str = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute",
            help="Total traveling time that is difference between the departure time of the first segment and the arrival time of the last segments for that particular entire set of connection.",
        )
    )


@dataclass
class LandCharges:
    """
    Prints non-air charges on a document.
    """

    tax: List[Tax] = field(
        default_factory=list,
        metadata=dict(
            name="Tax",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    base: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Base",
            type="Attribute",
            help=None,
        )
    )
    total: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Total",
            type="Attribute",
            help=None,
        )
    )
    miscellaneous: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Miscellaneous",
            type="Attribute",
            help=None,
        )
    )
    pre_paid: TypeMoney = field(
        default=None,
        metadata=dict(
            name="PrePaid",
            type="Attribute",
            help=None,
        )
    )
    deposit: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Deposit",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Leg:
    """
    Information about the journey Leg
    """

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata=dict(
            name="LegDetail",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    group: int = field(
        default=None,
        metadata=dict(
            name="Group",
            type="Attribute",
            help="Returns the Group Number for the leg.",
            required=True
        )
    )
    origin: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Returns the origin airport or city code for the leg.",
            required=True
        )
    )
    destination: TypeRailLocationCode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Returns the destination airport or city code for the leg.",
            required=True
        )
    )


@dataclass
class LegPrice:
    """
    Information about the journey Leg Price
    """

    leg_detail: List[LegDetail] = field(
        default_factory=list,
        metadata=dict(
            name="LegDetail",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute",
            help="The Total Prices for the Combination of Journey legs for this Price.",
            required=True
        )
    )
    approximate_total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute",
            help="The Converted Total Price in Agency's Default Currency Value",
        )
    )


@dataclass
class ManualFareAdjustment:
    applied_on: TypeAdjustmentTarget = field(
        default=None,
        metadata=dict(
            name="AppliedOn",
            type="Attribute",
            help="Represents pricing component upon which manual increment/discount to be applied. Presently supported values are Base and Total. Other is present as a future place holder but presently no request processing logic is available for value Other",
            required=True
        )
    )
    adjustment_type: TypeAdjustmentType = field(
        default=None,
        metadata=dict(
            name="AdjustmentType",
            type="Attribute",
            help="Represents process used for applying manual discount/increment. Presently supported values are Flat, Percentage.",
            required=True
        )
    )
    value: float = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help="Represents value of increment/discount applied. Negative value is considered as discount whereas positive value represents increment",
            required=True
        )
    )
    passenger_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="PassengerRef",
            type="Attribute",
            help="Represents passenger association.",
        )
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            help="Providers: 1p/1j",
        )
    )
    fare_type: TypeFareTypeCode = field(
        default=None,
        metadata=dict(
            name="FareType",
            type="Attribute",
            help="Providers: 1p/1j",
        )
    )


@dataclass
class MaxLayoverDurationType:
    """
    User can specify its attribute's value in Minutes. Maximum size of each attribute is 4.
    """

    domestic: MaxLayoverDurationRangeType = field(
        default=None,
        metadata=dict(
            name="Domestic",
            type="Attribute",
            help="It will be applied for all Domestic-to-Domestic connections.",
        )
    )
    gateway: MaxLayoverDurationRangeType = field(
        default=None,
        metadata=dict(
            name="Gateway",
            type="Attribute",
            help="It will be applied for all Domestic to International and International to Domestic connections.",
        )
    )
    international: MaxLayoverDurationRangeType = field(
        default=None,
        metadata=dict(
            name="International",
            type="Attribute",
            help="It will be applied for all International-to-International connections.",
        )
    )


@dataclass
class Meals(TypeMealService):
    """
    Available Meal Service.
    """

    pass


@dataclass
class OptionalServiceModifiers:
    """
    Rich Content and Branding for an optional service
    """

    optional_service_modifier: List[OptionalServiceModifier] = field(
        default_factory=list,
        metadata=dict(
            name="OptionalServiceModifier",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class OriginalItineraryDetails:
    """
    Used for rapid reprice to provide additional information about the original itinerary. Providers: 1G/1V/1P/1S/1A
    """

    itinerary_type: TypeItineraryCode = field(
        default=None,
        metadata=dict(
            name="ItineraryType",
            type="Attribute",
            help="Values allowed are International or Domestic. This tells if the itinerary is international or domestic.",
        )
    )
    bulk_ticket: bool = field(
        default="false",
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Set to true and the itinerary is/will be a bulk ticket. Set to false and the itinerary being repriced will not be a bulk ticket. Default is false.",
        )
    )
    ticketing_pcc: TypePcc = field(
        default=None,
        metadata=dict(
            name="TicketingPCC",
            type="Attribute",
            help="This is the PCC or SID where the ticket was issued",
        )
    )
    ticketing_iata: TypeIata = field(
        default=None,
        metadata=dict(
            name="TicketingIATA",
            type="Attribute",
            help="This is the IATA where the ticket was issued.",
        )
    )
    ticketing_country: TypeCountry = field(
        default=None,
        metadata=dict(
            name="TicketingCountry",
            type="Attribute",
            help="This is the country where the ticket was issued.",
        )
    )
    tour_code: TypeTourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            help=None,
        )
    )
    ticketing_date: str = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute",
            help="The date the repriced itinerary was ticketed",
        )
    )


@dataclass
class PassengerDetails:
    """
    Details of passenger
    """

    loyalty_card_details: List[LoyaltyCardDetails] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCardDetails",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=9
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Passenger key",
            required=True
        )
    )
    code: TypePtc = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="Passenger code",
            required=True
        )
    )
    age: int = field(
        default=None,
        metadata=dict(
            name="Age",
            type="Attribute",
            help="Passenger age",
        )
    )


@dataclass
class PassengerTicketNumber:
    """
    Information related to Ticket Number
    """

    ticket_number: TypePassengerTicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help="The identifying number for a Ticket for a passenger.",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="Reference to a passenger associated with a ticket.",
        )
    )


@dataclass
class Pcc:
    """
    Specify pseudo City
    """

    override_pcc: OverridePcc = field(
        default=None,
        metadata=dict(
            name="OverridePCC",
            type="Element",
            help=None,
        )
    )
    point_of_sale: List[PointOfSale] = field(
        default_factory=list,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=5
        )
    )
    ticket_agency: TicketAgency = field(
        default=None,
        metadata=dict(
            name="TicketAgency",
            type="Element",
            help=None,
        )
    )


@dataclass
class PenaltyFareInformation:
    penalty_info: TypeFarePenalty = field(
        default=None,
        metadata=dict(
            name="PenaltyInfo",
            type="Element",
            help="Penalty Limit if requested.",
        )
    )
    prohibit_penalty_fares: bool = field(
        default=None,
        metadata=dict(
            name="ProhibitPenaltyFares",
            type="Attribute",
            help="Indicates whether user wants penalty fares to be returned.",
            required=True
        )
    )


@dataclass
class PrePayId:
    """
    Pre pay unique identifier , example Flight Pass Number
    """

    company_name: CompanyName = field(
        default=None,
        metadata=dict(
            name="CompanyName",
            type="Element",
            help="Supplier info that is specific to the pre pay Id",
        )
    )
    id: TypeCardNumber = field(
        default=None,
        metadata=dict(
            name="Id",
            type="Attribute",
            help="This is the exact pre pay number. Example flight pass number",
            required=True
        )
    )
    type: str = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Type of pre pay unique identifier,presently only available value is FlightPass.",
        )
    )


@dataclass
class PrePayPriceInfo:
    """
    Pricing detail for the Pre Pay Account
    """

    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Detailed tax information for the pre pay account",
            min_occurs=0,
            max_occurs=999
        )
    )
    base_fare: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BaseFare",
            type="Attribute",
            help=None,
        )
    )
    total_fare: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalFare",
            type="Attribute",
            help=None,
        )
    )
    total_tax: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalTax",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class PreferredBookingCodes:
    """
    This is the container to specify all preferred booking codes
    """

    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class RefundFailureInfo:
    """
    Will be optionally returned as part of AirRefunTicketingRsp if one or all ticket refund requests fail.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            help="The identifying number for a Ticketless Air Reservation.",
            required=True
        )
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            required=True
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
            required=True
        )
    )
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    message: str = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class RelatedTraveler:
    """
    Detailed related Traveler information for pre pay profiles
    """

    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCard",
            type="Element",
            help="Traveler loyalty card detail",
            min_occurs=0,
            max_occurs=999
        )
    )
    person_name: PersonName = field(
        default=None,
        metadata=dict(
            name="PersonName",
            type="Element",
            help="Traveler name detail",
        )
    )
    credits_used: "RelatedTraveler.CreditsUsed" = field(
        default=None,
        metadata=dict(
            name="CreditsUsed",
            type="Element",
            help="Traveler pre pay credit detail",
        )
    )
    status_code: str = field(
        default=None,
        metadata=dict(
            name="StatusCode",
            type="Attribute",
            help="Traveler status code(One of Marked for deletion,Lapsed,Terminated,Active,Inactive)",
        )
    )
    relation: str = field(
        default=None,
        metadata=dict(
            name="Relation",
            type="Attribute",
            help="Relation to the pre pay id. Example flight pass user",
        )
    )

    @dataclass
    class CreditsUsed:
        used_credit: float = field(
            default=None,
            metadata=dict(
                name="UsedCredit",
                type="Attribute",
                help=None,
            )
        )
        currency_code: TypeCurrency = field(
            default=None,
            metadata=dict(
                name="CurrencyCode",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class RuleAdvancedPurchase:
    """
    Container for rules regarding advance purchase restrictions. TicketingEarliestDate and TicketingLatestDate are strings representing respective dates. If a year component is present then it signifies an exact date. If only day and month components are present then it signifies a seasonal date, which means applicable for that date in any year
    """

    reservation_latest_period: str = field(
        default=None,
        metadata=dict(
            name="ReservationLatestPeriod",
            type="Attribute",
            help=None,
        )
    )
    reservation_latest_unit: TypeStayUnit = field(
        default=None,
        metadata=dict(
            name="ReservationLatestUnit",
            type="Attribute",
            help=None,
        )
    )
    ticketing_earliest_date: str = field(
        default=None,
        metadata=dict(
            name="TicketingEarliestDate",
            type="Attribute",
            help=None,
        )
    )
    ticketing_latest_date: str = field(
        default=None,
        metadata=dict(
            name="TicketingLatestDate",
            type="Attribute",
            help=None,
        )
    )
    more_rules_present: bool = field(
        default=None,
        metadata=dict(
            name="MoreRulesPresent",
            type="Attribute",
            help="If true, specifies that advance purchase information will be present in fare rules.",
        )
    )


@dataclass
class SegmentSelect:
    """
    To be used to pass the selected segment.
    """

    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help="Reference to AirSegment from an Air Reservation.",
            min_occurs=0,
            max_occurs=999
        )
    )
    hotel_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata=dict(
            name="HotelReservationRef",
            type="Element",
            help="Specify the locator code of Hotel reservation if it needs to be considered as Auxiliary segment",
            min_occurs=0,
            max_occurs=999
        )
    )
    vehicle_reservation_ref: List[TypeNonAirReservationRef] = field(
        default_factory=list,
        metadata=dict(
            name="VehicleReservationRef",
            type="Element",
            help="Specify the locator code of Vehicle reservation if it needs to be considered as Auxiliary segment",
            min_occurs=0,
            max_occurs=999
        )
    )
    passive_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PassiveSegmentRef",
            type="Element",
            help="Reference to PassiveSegment from a Passive Reservation.Specify the passive segment if it needs to be considered as Auxiliary segment",
            min_occurs=0,
            max_occurs=999
        )
    )
    all_confirmed_air: bool = field(
        default=None,
        metadata=dict(
            name="AllConfirmedAir",
            type="Attribute",
            help="Set to true to consider all Confirmed segments including active and passive and set to false to discard confirmed segments",
        )
    )
    all_waitlisted_air: bool = field(
        default=None,
        metadata=dict(
            name="AllWaitlistedAir",
            type="Attribute",
            help="Set to true to consider all Waitlisted segments and false to discard all waitlisted segments",
        )
    )
    all_hotel: bool = field(
        default=None,
        metadata=dict(
            name="AllHotel",
            type="Attribute",
            help="Set to true to consider all Hotel reservations as Auxiliary segment and false to discard all Hotel reservations",
        )
    )
    all_vehicle: bool = field(
        default=None,
        metadata=dict(
            name="AllVehicle",
            type="Attribute",
            help=None,
        )
    )
    all_passive: bool = field(
        default=None,
        metadata=dict(
            name="AllPassive",
            type="Attribute",
            help="Set to true to consider all Passive segments as Auxiliary segment and false to discard passive segments",
        )
    )


@dataclass
class SelectionModifiers:
    """
    Modifiers supported for selection of services during EMD Issuance. Supported providers are 1V/1G/1P/1J
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help="References to airsegments for which EMDs will be generated on all the associated services.",
            min_occurs=0,
            max_occurs=999
        )
    )
    svc_segment_ref: List[TypeRef] = field(
        default_factory=list,
        metadata=dict(
            name="SvcSegmentRef",
            type="Element",
            help="SVC segment reference to which the EMD is being issued",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_code: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Supplier/Vendor code for which EMDs will be generated on all the associated services. Required if PNR contains more than one supplier.",
        )
    )
    rfic: str = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute",
            help="Reason for issuance code for which EMDs will be generated on all the associated services.",
            length=1
        )
    )


@dataclass
class ServiceGroup:
    """
    The Service Group of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH
    """

    service_sub_group: List[ServiceSubGroup] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceSubGroup",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=15
        )
    )
    code: str = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help="The Service Group Code of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
            required=True
        )
    )


@dataclass
class SolutionGroup:
    """
    Specifies the trip type and diversity of all or a subset of the result solutions.
    """

    permitted_account_codes: "SolutionGroup.PermittedAccountCodes" = field(
        default=None,
        metadata=dict(
            name="PermittedAccountCodes",
            type="Element",
            help=None,
        )
    )
    preferred_account_codes: "SolutionGroup.PreferredAccountCodes" = field(
        default=None,
        metadata=dict(
            name="PreferredAccountCodes",
            type="Element",
            help=None,
        )
    )
    prohibited_account_codes: "SolutionGroup.ProhibitedAccountCodes" = field(
        default=None,
        metadata=dict(
            name="ProhibitedAccountCodes",
            type="Element",
            help=None,
        )
    )
    permitted_point_of_sales: "SolutionGroup.PermittedPointOfSales" = field(
        default=None,
        metadata=dict(
            name="PermittedPointOfSales",
            type="Element",
            help=None,
        )
    )
    prohibited_point_of_sales: "SolutionGroup.ProhibitedPointOfSales" = field(
        default=None,
        metadata=dict(
            name="ProhibitedPointOfSales",
            type="Element",
            help=None,
        )
    )
    count: int = field(
        default=None,
        metadata=dict(
            name="Count",
            type="Attribute",
            help="The number of solution to include in this group. If only one group specified, this can be left blank. If multiple groups specified, all counts must add up to the MaxResults of the request.",
        )
    )
    trip_type: TypeTripType = field(
        default=None,
        metadata=dict(
            name="TripType",
            type="Attribute",
            help="Specifies the trip type for this group of results. Allows targeting a result set to a particular set of characterists.",
            required=True
        )
    )
    diversification: TypeDiversity = field(
        default=None,
        metadata=dict(
            name="Diversification",
            type="Attribute",
            help="Specifies the diversification of this group of results, if specified. Allows targeting a result set to ensure they contain more unique results.",
        )
    )
    tag: str = field(
        default=None,
        metadata=dict(
            name="Tag",
            type="Attribute",
            help="An arbitrary name for this group of solutions. Will be returned with the solution for idetification.",
            max_length=20.0
        )
    )
    primary: bool = field(
        default="false",
        metadata=dict(
            name="Primary",
            type="Attribute",
            help="Indicates that this is a primary SolutionGroup when using alternate pricing concepts",
        )
    )

    @dataclass
    class PermittedAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedAccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PermittedPointOfSales:
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata=dict(
                name="PointOfSale",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedPointOfSales:
        point_of_sale: List[PointOfSale] = field(
            default_factory=list,
            metadata=dict(
                name="PointOfSale",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class SvcSegment:
    """
    Service segment added to collect additional fee. 1P only
    """

    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="The Key of SVC Segment.",
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="The platting carrier",
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
        )
    )
    number_of_items: int = field(
        default=None,
        metadata=dict(
            name="NumberOfItems",
            type="Attribute",
            help=None,
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Origin location - Airport code. 1P only.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Destination location - Airport code. 1P only.",
        )
    )
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help="Start date of the segment. Generally it is the next date after the last air segment. 1P only",
        )
    )
    travel_order: int = field(
        default=None,
        metadata=dict(
            name="TravelOrder",
            type="Attribute",
            help="To identify the appropriate travel sequence for Air/Car/Hotel/Passive segments/reservations based on travel dates. This ordering is applicable across the UR not provider or traveler specific",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help=None,
        )
    )
    rfic: str = field(
        default=None,
        metadata=dict(
            name="RFIC",
            type="Attribute",
            help="1P - Reason for issuance",
        )
    )
    rfisc: str = field(
        default=None,
        metadata=dict(
            name="RFISC",
            type="Attribute",
            help="1P - Resaon for issuance sub-code",
        )
    )
    svc_description: str = field(
        default=None,
        metadata=dict(
            name="SvcDescription",
            type="Attribute",
            help="1P - SVC fee description",
        )
    )
    fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Fee",
            type="Attribute",
            help="The fee to be collected using SVC segment",
        )
    )
    emdnumber: TypeEmdnumber = field(
        default=None,
        metadata=dict(
            name="EMDNumber",
            type="Attribute",
            help="Generated EMD number, if EMD is issued on the SVC",
        )
    )


@dataclass
class TcrexchangeBundle:
    """
    Used in AirExchangeReq request and AirExchangeQuoteRsp response
    """

    air_exchange_info: AirExchangeInfo = field(
        default=None,
        metadata=dict(
            name="AirExchangeInfo",
            type="Element",
            help=None,
            required=True
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Itinerary level taxes",
            min_occurs=0,
            max_occurs=999
        )
    )
    penalty: List[Penalty] = field(
        default_factory=list,
        metadata=dict(
            name="Penalty",
            type="Element",
            help="Only used within an AirExchangeQuoteRsp",
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            help="The identifying number for a Ticketless Air Reservation.",
            required=True
        )
    )


@dataclass
class Tcrinfo:
    status: TypeTcrstatus = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
            required=True
        )
    )
    date: str = field(
        default=None,
        metadata=dict(
            name="Date",
            type="Attribute",
            help=None,
        )
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            help="The identifying number for a Ticketless Air Reservation.",
            required=True
        )
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
            required=True
        )
    )


@dataclass
class TermConditions:
    """
    The terms and conditions to be included in Fax details
    """

    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata=dict(
            name="LanguageOption",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    include_term_conditions: bool = field(
        default=None,
        metadata=dict(
            name="IncludeTermConditions",
            type="Attribute",
            help="Specifies whether Term and Conditions included in the Fax or not .",
            required=True
        )
    )


@dataclass
class Text(TypeTextElement):
    """
    Type of Text, Eg-'Upsell','Marketing Agent','Marketing Consumer','Strapline','Rule'.
    """

    pass


@dataclass
class TicketDesignator:
    """
    Ticket Designator used to further qualify a Fare Basis Code.
    """

    value: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TicketFailureInfo:
    """
    Will be optionally returned as part of AirTicketingRsp if one or all ticket requests fail. Atrributes are faiilure code, failure message, and passenger reference key. Passenger name is a child element.
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help="Returns related air pricing infos.",
            min_occurs=1,
            max_occurs=999
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
            required=True
        )
    )
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    message: str = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            help=None,
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TicketInfo:
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
            required=True
        )
    )
    conjuncted_ticket_info: List[ConjunctedTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ConjunctedTicketInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangedTicketInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    number: str = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            required=True
        )
    )
    iatanumber: TypeIata = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            help=None,
        )
    )
    ticket_issue_date: str = field(
        default=None,
        metadata=dict(
            name="TicketIssueDate",
            type="Attribute",
            help=None,
        )
    )
    ticketing_agent_sign_on: str = field(
        default=None,
        metadata=dict(
            name="TicketingAgentSignOn",
            type="Attribute",
            help=None,
            max_length=8.0
        )
    )
    country_code: TypeCountry = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            help="Contains Ticketed PCC’s Country code.",
        )
    )
    status: TypeTicketStatus = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help=None,
            required=True
        )
    )
    bulk_ticket: bool = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Whether the ticket was issued as bulk.",
        )
    )
    booking_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="BookingTravelerRef",
            type="Attribute",
            help="A reference to a passenger.",
            required=True
        )
    )
    air_pricing_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Attribute",
            help="A reference to a AirPricing.Applicable Providers 1G and 1V.",
        )
    )


@dataclass
class Title(TypeTextElement):
    """
    The additional titles associated to the brand or optional service. Providers: ACH, RCH, 1G, 1V, 1P, 1J.
    """

    pass


@dataclass
class TourCode:
    """
    Tour Code Fare Basis
    """

    value: TypeTourCode = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeRestrictionLengthOfStay:
    """
    Length Of Stay Restriction ( e.g. 2 day minimum..)
    """

    length: int = field(
        default=None,
        metadata=dict(
            name="Length",
            type="Attribute",
            help=None,
        )
    )
    stay_unit: TypeStayUnit = field(
        default=None,
        metadata=dict(
            name="StayUnit",
            type="Attribute",
            help=None,
        )
    )
    stay_date: str = field(
        default=None,
        metadata=dict(
            name="StayDate",
            type="Attribute",
            help=None,
        )
    )
    more_rules_present: bool = field(
        default=None,
        metadata=dict(
            name="MoreRulesPresent",
            type="Attribute",
            help="If true, specifies that advance purchase information will be present in fare rules.",
        )
    )


@dataclass
class TypeTaxInfoWithPaymentRef(TypeTaxInfo):
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRef",
            type="Element",
            help="This reference elements will associate relevant payment to this tax",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class TypeTicketFailureInfo:
    """
    Will be optionally returned as part if one or all ticketing requests fail.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Element",
            help="The identifying number for a Ticketless Air Reservation.",
            required=True
        )
    )
    ticket_number: TicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            required=True
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
            required=True
        )
    )
    code: int = field(
        default=None,
        metadata=dict(
            name="Code",
            type="Attribute",
            help=None,
            required=True
        )
    )
    message: str = field(
        default=None,
        metadata=dict(
            name="Message",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class TypeTicketingModifiersRef:
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class TypeWeight:
    value: int = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
        )
    )
    unit: TypeUnitWeight = field(
        default=None,
        metadata=dict(
            name="Unit",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class Variance:
    """
    Indicates any variance in the requested flight.
    """

    type: TypeVarianceType = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Indicates type Variance, i.e. Actual, Estimated, Canceled and Diversion.",
            required=True
        )
    )
    time: str = field(
        default=None,
        metadata=dict(
            name="Time",
            type="Attribute",
            help="Indicates time for Variance.",
        )
    )
    indicator: TypeVarianceIndicator = field(
        default=None,
        metadata=dict(
            name="Indicator",
            type="Attribute",
            help="Indicates VAriance Indicator, i.e. Early, Late.",
        )
    )
    reason: str = field(
        default=None,
        metadata=dict(
            name="Reason",
            type="Attribute",
            help="Reason for Variance",
        )
    )


@dataclass
class WaiverCode:
    """
    Waiver code to override fare validations
    """

    tour_code: TypeTourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            help=None,
        )
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Attribute",
            help=None,
        )
    )
    endorsement: str = field(
        default=None,
        metadata=dict(
            name="Endorsement",
            type="Attribute",
            help="Endorsement. Size can be up to 100 characters",
            min_length=0.0,
            max_length=100.0
        )
    )


@dataclass
class AirExchangeBundleList:
    """
    The shared object list of AirsegmentData
    """

    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeTicketBundle:
    ticket_number: TicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Element",
            help=None,
            required=True
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    form_of_payment_ref: FormOfPaymentRef = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            help=None,
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )


@dataclass
class AirFareDisplayModifiers:
    trip_type: List[TypeFareTripType] = field(
        default_factory=list,
        metadata=dict(
            name="TripType",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    cabin_class: CabinClass = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help=None,
        )
    )
    penalty_fare_information: PenaltyFareInformation = field(
        default=None,
        metadata=dict(
            name="PenaltyFareInformation",
            type="Element",
            help="Request Fares with specific Penalty Information.",
        )
    )
    fare_search_option: List[TypeFareSearchOption] = field(
        default_factory=list,
        metadata=dict(
            name="FareSearchOption",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=5
        )
    )
    max_responses: int = field(
        default="200",
        metadata=dict(
            name="MaxResponses",
            type="Attribute",
            help=None,
        )
    )
    departure_date: str = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            help=None,
        )
    )
    ticketing_date: str = field(
        default=None,
        metadata=dict(
            name="TicketingDate",
            type="Attribute",
            help=None,
        )
    )
    return_date: str = field(
        default=None,
        metadata=dict(
            name="ReturnDate",
            type="Attribute",
            help=None,
        )
    )
    base_fare_only: bool = field(
        default="false",
        metadata=dict(
            name="BaseFareOnly",
            type="Attribute",
            help=None,
        )
    )
    unrestricted_fares_only: bool = field(
        default="false",
        metadata=dict(
            name="UnrestrictedFaresOnly",
            type="Attribute",
            help=None,
        )
    )
    fares_indicator: TypeFaresIndicator = field(
        default=None,
        metadata=dict(
            name="FaresIndicator",
            type="Attribute",
            help="Indicates whether only public fares should be returned or specific type of private fares",
        )
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help=None,
        )
    )
    include_taxes: bool = field(
        default=None,
        metadata=dict(
            name="IncludeTaxes",
            type="Attribute",
            help=None,
        )
    )
    include_estimated_taxes: bool = field(
        default=None,
        metadata=dict(
            name="IncludeEstimatedTaxes",
            type="Attribute",
            help="Indicates to include estimated taxes i.e. if set to true estimated total fare,base fare and taxes would be returned.",
        )
    )
    include_surcharges: bool = field(
        default=None,
        metadata=dict(
            name="IncludeSurcharges",
            type="Attribute",
            help=None,
        )
    )
    global_indicator: TypeAtpcoglobalIndicator = field(
        default=None,
        metadata=dict(
            name="GlobalIndicator",
            type="Attribute",
            help=None,
        )
    )
    prohibit_min_stay_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitMinStayFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_max_stay_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitMaxStayFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_advance_purchase_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitAdvancePurchaseFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute",
            help="Indicates whether it prohibits NonRefundable Fares.",
        )
    )
    validated_fares_only: bool = field(
        default=None,
        metadata=dict(
            name="ValidatedFaresOnly",
            type="Attribute",
            help="Indicates that the requested Fares should be Validated Fares only. If set to true, then only valid fares will be returned. If set to false, both valid and non valid fares will be returned. If not sent, then no validation will be done. All fares will be returned.",
        )
    )
    prohibit_travel_restricted_fares: bool = field(
        default="true",
        metadata=dict(
            name="ProhibitTravelRestrictedFares",
            type="Attribute",
            help="Indicates that the Fares not complying Travel Restrictions and Seasonality fare rules are prohibited",
        )
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            help="Represents the filed currency of the fare",
        )
    )


@dataclass
class AirFareRulesModifier:
    """
    The modifiers for Air Fare Rules
    """

    air_fare_rule_category: List[AirFareRuleCategory] = field(
        default_factory=list,
        metadata=dict(
            name="AirFareRuleCategory",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirItineraryDetails:
    """
    Itinerary details containing brand details
    """

    air_segment_details: List[AirSegmentDetails] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentDetails",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=16
        )
    )
    passenger_details: List[PassengerDetails] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerDetails",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=15
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Air itinerary details key",
            required=True
        )
    )


@dataclass
class AirItinerarySolution:
    """
    The pricing container for an air travel itinerary
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata=dict(
            name="Connection",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class AirLegModifiers:
    permitted_cabins: PermittedCabins = field(
        default=None,
        metadata=dict(
            name="PermittedCabins",
            type="Element",
            help=None,
        )
    )
    preferred_cabins: PreferredCabins = field(
        default=None,
        metadata=dict(
            name="PreferredCabins",
            type="Element",
            help=None,
        )
    )
    permitted_carriers: PermittedCarriers = field(
        default=None,
        metadata=dict(
            name="PermittedCarriers",
            type="Element",
            help=None,
        )
    )
    prohibited_carriers: ProhibitedCarriers = field(
        default=None,
        metadata=dict(
            name="ProhibitedCarriers",
            type="Element",
            help=None,
        )
    )
    preferred_carriers: PreferredCarriers = field(
        default=None,
        metadata=dict(
            name="PreferredCarriers",
            type="Element",
            help=None,
        )
    )
    permitted_connection_points: "AirLegModifiers.PermittedConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="PermittedConnectionPoints",
            type="Element",
            help="This is the container to specify all permitted connection points. Applicable for 1G/1V/1P/1J.",
        )
    )
    prohibited_connection_points: "AirLegModifiers.ProhibitedConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="ProhibitedConnectionPoints",
            type="Element",
            help="This is the container to specify all prohibited connection points. Applicable for 1G/1V/1P/1J.",
        )
    )
    preferred_connection_points: "AirLegModifiers.PreferredConnectionPoints" = field(
        default=None,
        metadata=dict(
            name="PreferredConnectionPoints",
            type="Element",
            help="This is the container to specify all preferred connection points. Applicable for 1G/1V only.",
        )
    )
    permitted_booking_codes: "AirLegModifiers.PermittedBookingCodes" = field(
        default=None,
        metadata=dict(
            name="PermittedBookingCodes",
            type="Element",
            help="This is the container to specify all permitted booking codes",
        )
    )
    preferred_booking_codes: PreferredBookingCodes = field(
        default=None,
        metadata=dict(
            name="PreferredBookingCodes",
            type="Element",
            help=None,
        )
    )
    preferred_alliances: "AirLegModifiers.PreferredAlliances" = field(
        default=None,
        metadata=dict(
            name="PreferredAlliances",
            type="Element",
            help=None,
        )
    )
    prohibited_booking_codes: "AirLegModifiers.ProhibitedBookingCodes" = field(
        default=None,
        metadata=dict(
            name="ProhibitedBookingCodes",
            type="Element",
            help="This is the container to specify all prohibited booking codes",
        )
    )
    disfavored_alliances: "AirLegModifiers.DisfavoredAlliances" = field(
        default=None,
        metadata=dict(
            name="DisfavoredAlliances",
            type="Element",
            help=None,
        )
    )
    flight_type: FlightType = field(
        default=None,
        metadata=dict(
            name="FlightType",
            type="Element",
            help=None,
        )
    )
    anchor_flight_data: TypeAnchorFlightData = field(
        default=None,
        metadata=dict(
            name="AnchorFlightData",
            type="Element",
            help=None,
        )
    )
    prohibit_overnight_layovers: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitOvernightLayovers",
            type="Attribute",
            help="If true, excludes connections if arrival time of first flight and departure time of second flight is on 2 different calendar days. When used in conjunction with MaxConnectionTime, it would exclude all connections if the connecting flights wait time exceeds the time specified in MaxConnectionTime.",
        )
    )
    max_connection_time: int = field(
        default=None,
        metadata=dict(
            name="MaxConnectionTime",
            type="Attribute",
            help=None,
        )
    )
    return_first_available_only: bool = field(
        default=None,
        metadata=dict(
            name="ReturnFirstAvailableOnly",
            type="Attribute",
            help="If it is true then it will search for first available for the booking code designated or any booking code in same cabin.",
        )
    )
    allow_direct_access: bool = field(
        default="false",
        metadata=dict(
            name="AllowDirectAccess",
            type="Attribute",
            help="If it is true request will be sent directly to the carrier.",
        )
    )
    prohibit_multi_airport_connection: bool = field(
        default=None,
        metadata=dict(
            name="ProhibitMultiAirportConnection",
            type="Attribute",
            help="Indicates whether to restrict multi-airport connections",
        )
    )
    prefer_non_stop: bool = field(
        default="false",
        metadata=dict(
            name="PreferNonStop",
            type="Attribute",
            help="When non-stops are preferred, the distribution of search results should skew heavily toward non-stop flights while still returning some one stop flights for comparison and price competitiveness. The search request will ‘boost' the preference towards non-stops. If true then Non Stop flights will be preferred.",
        )
    )
    order_by: str = field(
        default=None,
        metadata=dict(
            name="OrderBy",
            type="Attribute",
            help="Indicates whether to sort by Journey Time, Deparature Time or Arrival Time",
        )
    )
    max_journey_time: TypeMaxJourneyTime = field(
        default=None,
        metadata=dict(
            name="MaxJourneyTime",
            type="Attribute",
            help="Maximum Journey Time for this leg (in hours) 0-99. Supported Providers 1G,1V.",
        )
    )

    @dataclass
    class PermittedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredConnectionPoints:
        connection_point: List[ConnectionPoint] = field(
            default_factory=list,
            metadata=dict(
                name="ConnectionPoint",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=99
            )
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirPricingModifiers:
    """
    Controls and switches for a Air Search request that contains Pricing Information
    """

    prohibited_rule_categories: "AirPricingModifiers.ProhibitedRuleCategories" = field(
        default=None,
        metadata=dict(
            name="ProhibitedRuleCategories",
            type="Element",
            help=None,
        )
    )
    account_codes: "AirPricingModifiers.AccountCodes" = field(
        default=None,
        metadata=dict(
            name="AccountCodes",
            type="Element",
            help=None,
        )
    )
    permitted_cabins: PermittedCabins = field(
        default=None,
        metadata=dict(
            name="PermittedCabins",
            type="Element",
            help=None,
        )
    )
    contract_codes: "AirPricingModifiers.ContractCodes" = field(
        default=None,
        metadata=dict(
            name="ContractCodes",
            type="Element",
            help=None,
        )
    )
    exempt_taxes: ExemptTaxes = field(
        default=None,
        metadata=dict(
            name="ExemptTaxes",
            type="Element",
            help=None,
        )
    )
    penalty_fare_information: PenaltyFareInformation = field(
        default=None,
        metadata=dict(
            name="PenaltyFareInformation",
            type="Element",
            help="Request Fares with specific Penalty Information.",
        )
    )
    discount_card: List[DiscountCard] = field(
        default_factory=list,
        metadata=dict(
            name="DiscountCard",
            type="Element",
            help="Discount request for rail.",
            min_occurs=0,
            max_occurs=9
        )
    )
    promo_codes: "AirPricingModifiers.PromoCodes" = field(
        default=None,
        metadata=dict(
            name="PromoCodes",
            type="Element",
            help=None,
        )
    )
    manual_fare_adjustment: List[ManualFareAdjustment] = field(
        default_factory=list,
        metadata=dict(
            name="ManualFareAdjustment",
            type="Element",
            help="Represents increment/discount applied manually by agent.",
            min_occurs=0,
            max_occurs=999
        )
    )
    point_of_sale: PointOfSale = field(
        default=None,
        metadata=dict(
            name="PointOfSale",
            type="Element",
            help="User can use this node to send a specific PCC to access fares allowed only for that PCC. This node gives the capability for fare redistribution at stored fare level. As multiple UAPI AirPricingInfos (all having same AirPricingInfoGroup) can converge to a single stored fare, UAPI will map PoinOfSale information from the first available one from each group",
        )
    )
    brand_modifiers: BrandModifiers = field(
        default=None,
        metadata=dict(
            name="BrandModifiers",
            type="Element",
            help="Used to specify the level of branding requested.",
        )
    )
    multi_gdssearch_indicator: List[MultiGdssearchIndicator] = field(
        default_factory=list,
        metadata=dict(
            name="MultiGDSSearchIndicator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    preferred_cabins: List[PreferredCabins] = field(
        default_factory=list,
        metadata=dict(
            name="PreferredCabins",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    prohibit_min_stay_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitMinStayFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_max_stay_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitMaxStayFares",
            type="Attribute",
            help=None,
        )
    )
    currency_type: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="CurrencyType",
            type="Attribute",
            help=None,
        )
    )
    prohibit_advance_purchase_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitAdvancePurchaseFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_non_refundable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonRefundableFares",
            type="Attribute",
            help=None,
        )
    )
    prohibit_restricted_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitRestrictedFares",
            type="Attribute",
            help=None,
        )
    )
    fares_indicator: TypeFaresIndicator = field(
        default=None,
        metadata=dict(
            name="FaresIndicator",
            type="Attribute",
            help="Indicates whether only public fares should be returned or specific type of private fares",
        )
    )
    filed_currency: TypeCurrency = field(
        default=None,
        metadata=dict(
            name="FiledCurrency",
            type="Attribute",
            help="Currency in which Fares/Prices will be filed if supported by the supplier else approximated to.",
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="The Plating Carrier for this journey.",
        )
    )
    override_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="OverrideCarrier",
            type="Attribute",
            help="The Plating Carrier for this journey.",
        )
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute",
            help="Request a search based on whether only E-ticketable fares are required.",
        )
    )
    account_code_fares_only: bool = field(
        default=None,
        metadata=dict(
            name="AccountCodeFaresOnly",
            type="Attribute",
            help="Indicates whether or not the private fares returned should be restricted to only those specific to the input account code and contract code.",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    prohibit_non_exchangeable_fares: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitNonExchangeableFares",
            type="Attribute",
            help=None,
        )
    )
    force_segment_select: bool = field(
        default="false",
        metadata=dict(
            name="ForceSegmentSelect",
            type="Attribute",
            help="This indicator allows agent to force segment select option in host while selecting all air segments to store price on a PNR. This is relevent only when agent selects all air segmnets to price. if agent selects specific segments to price then this attribute will be ignored by the system. This is currently used by Worldspan only.",
        )
    )
    inventory_request_type: TypeInventoryRequest = field(
        default=None,
        metadata=dict(
            name="InventoryRequestType",
            type="Attribute",
            help="This allows user to make request for a particular source of inventory for pricing modifier purposes. This is currently used by Worldspan only.",
        )
    )
    one_way_shop: bool = field(
        default="false",
        metadata=dict(
            name="OneWayShop",
            type="Attribute",
            help="Via this attribute one way shop can be requested. Applicable provider is 1G",
        )
    )
    prohibit_unbundled_fare_types: bool = field(
        default=None,
        metadata=dict(
            name="ProhibitUnbundledFareTypes",
            type="Attribute",
            help="A 'True' value wiill remove fares with EOU and ERU fare types from consideration. A 'False' value is the same as no value. Default is no value. Applicable providers: 1P/1J/1G/1V",
        )
    )
    return_services: bool = field(
        default="true",
        metadata=dict(
            name="ReturnServices",
            type="Attribute",
            help="When set to false, ATPCO filed Optional Services will not be returned. Default is true. Provider: 1G, 1V, 1P, 1J",
        )
    )
    channel_id: str = field(
        default=None,
        metadata=dict(
            name="ChannelId",
            type="Attribute",
            help="A Channel ID is 2 to 4 alpha-numeric characters used to activate the Search Control Console filter for a specific group of travelers being served by the agency credential.",
            min_length=2.0,
            max_length=4.0
        )
    )
    return_fare_attributes: bool = field(
        default="false",
        metadata=dict(
            name="ReturnFareAttributes",
            type="Attribute",
            help="Returns attributes that are associated to a fare",
        )
    )
    sell_check: bool = field(
        default="false",
        metadata=dict(
            name="SellCheck",
            type="Attribute",
            help="Checks if the segment is bookable before pricing",
        )
    )
    return_failed_segments: bool = field(
        default="false",
        metadata=dict(
            name="ReturnFailedSegments",
            type="Attribute",
            help="If 'true', returns failed segments information.",
        )
    )

    @dataclass
    class ProhibitedRuleCategories:
        fare_rule_category: List[FareRuleCategory] = field(
            default_factory=list,
            metadata=dict(
                name="FareRuleCategory",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class AccountCodes:
        account_code: List[AccountCode] = field(
            default_factory=list,
            metadata=dict(
                name="AccountCode",
                type="Element",
                help="Used to get negotiated pricing. Provider:ACH.",
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ContractCodes:
        contract_code: List[ContractCode] = field(
            default_factory=list,
            metadata=dict(
                name="ContractCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PromoCodes:
        promo_code: List[PromoCode] = field(
            default_factory=list,
            metadata=dict(
                name="PromoCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirRefundBundle:
    """
    Used both in request and response
    """

    air_refund_info: AirRefundInfo = field(
        default=None,
        metadata=dict(
            name="AirRefundInfo",
            type="Element",
            help=None,
            required=True
        )
    )
    name: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="Name",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )
    ticket_number: str = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help=None,
        )
    )
    ptc: str = field(
        default=None,
        metadata=dict(
            name="PTC",
            type="Attribute",
            help="Specifies the passenger type code for 1P",
        )
    )
    refund_type: str = field(
        default=None,
        metadata=dict(
            name="RefundType",
            type="Attribute",
            help="Specifies whether this bundle was auto or manually generated",
        )
    )


@dataclass
class AirSearchModifiers:
    """
    Controls and switches for the Air Search request
    """

    disfavored_providers: "AirSearchModifiers.DisfavoredProviders" = field(
        default=None,
        metadata=dict(
            name="DisfavoredProviders",
            type="Element",
            help=None,
        )
    )
    preferred_providers: "AirSearchModifiers.PreferredProviders" = field(
        default=None,
        metadata=dict(
            name="PreferredProviders",
            type="Element",
            help=None,
        )
    )
    disfavored_carriers: "AirSearchModifiers.DisfavoredCarriers" = field(
        default=None,
        metadata=dict(
            name="DisfavoredCarriers",
            type="Element",
            help=None,
        )
    )
    permitted_carriers: PermittedCarriers = field(
        default=None,
        metadata=dict(
            name="PermittedCarriers",
            type="Element",
            help=None,
        )
    )
    prohibited_carriers: ProhibitedCarriers = field(
        default=None,
        metadata=dict(
            name="ProhibitedCarriers",
            type="Element",
            help=None,
        )
    )
    preferred_carriers: PreferredCarriers = field(
        default=None,
        metadata=dict(
            name="PreferredCarriers",
            type="Element",
            help=None,
        )
    )
    permitted_cabins: PermittedCabins = field(
        default=None,
        metadata=dict(
            name="PermittedCabins",
            type="Element",
            help=None,
        )
    )
    preferred_cabins: PreferredCabins = field(
        default=None,
        metadata=dict(
            name="PreferredCabins",
            type="Element",
            help=None,
        )
    )
    preferred_alliances: "AirSearchModifiers.PreferredAlliances" = field(
        default=None,
        metadata=dict(
            name="PreferredAlliances",
            type="Element",
            help=None,
        )
    )
    disfavored_alliances: "AirSearchModifiers.DisfavoredAlliances" = field(
        default=None,
        metadata=dict(
            name="DisfavoredAlliances",
            type="Element",
            help=None,
        )
    )
    permitted_booking_codes: "AirSearchModifiers.PermittedBookingCodes" = field(
        default=None,
        metadata=dict(
            name="PermittedBookingCodes",
            type="Element",
            help="This is the container to specify all permitted booking codes",
        )
    )
    preferred_booking_codes: PreferredBookingCodes = field(
        default=None,
        metadata=dict(
            name="PreferredBookingCodes",
            type="Element",
            help=None,
        )
    )
    prohibited_booking_codes: "AirSearchModifiers.ProhibitedBookingCodes" = field(
        default=None,
        metadata=dict(
            name="ProhibitedBookingCodes",
            type="Element",
            help="This is the container to specify all prohibited booking codes",
        )
    )
    flight_type: FlightType = field(
        default=None,
        metadata=dict(
            name="FlightType",
            type="Element",
            help=None,
        )
    )
    max_layover_duration: MaxLayoverDurationType = field(
        default=None,
        metadata=dict(
            name="MaxLayoverDuration",
            type="Element",
            help="This is the maximum duration the layover may have for each trip in the request. Supported providers 1P, 1J.",
        )
    )
    native_search_modifier: TypeNativeSearchModifier = field(
        default=None,
        metadata=dict(
            name="NativeSearchModifier",
            type="Element",
            help="Container for Native command modifiers. Providers supported : 1P",
        )
    )
    distance_type: TypeDistance = field(
        default="MI",
        metadata=dict(
            name="DistanceType",
            type="Attribute",
            help=None,
        )
    )
    include_flight_details: bool = field(
        default="true",
        metadata=dict(
            name="IncludeFlightDetails",
            type="Attribute",
            help=None,
        )
    )
    allow_change_of_airport: bool = field(
        default="true",
        metadata=dict(
            name="AllowChangeOfAirport",
            type="Attribute",
            help=None,
        )
    )
    prohibit_overnight_layovers: bool = field(
        default="false",
        metadata=dict(
            name="ProhibitOvernightLayovers",
            type="Attribute",
            help="If true, excludes connections if arrival time of first flight and departure time of second flight is on 2 different calendar days. When used in conjunction with MaxConnectionTime, it would exclude all connections if the connecting flights wait time exceeds the time specified in MaxConnectionTime.",
        )
    )
    max_solutions: int = field(
        default=None,
        metadata=dict(
            name="MaxSolutions",
            type="Attribute",
            help="The maximum number of solutions to return. Decreasing this number",
        )
    )
    max_connection_time: int = field(
        default=None,
        metadata=dict(
            name="MaxConnectionTime",
            type="Attribute",
            help="The maximum anount of time (in minutes) that a solution can contain for connections between flights.",
        )
    )
    search_weekends: bool = field(
        default=None,
        metadata=dict(
            name="SearchWeekends",
            type="Attribute",
            help="A value of true indicates that search should be expanded to include weekend combinations, if applicable.",
        )
    )
    include_extra_solutions: bool = field(
        default=None,
        metadata=dict(
            name="IncludeExtraSolutions",
            type="Attribute",
            help="If true, indicates that search should be made for returning more solutions, if available. For example, for certain providers, premium members may have the facility to get more solutions. This attribute may have to be combined with other applicable modifiers (like SearchWeekends) to return more results.",
        )
    )
    prohibit_multi_airport_connection: bool = field(
        default=None,
        metadata=dict(
            name="ProhibitMultiAirportConnection",
            type="Attribute",
            help="Indicates whether to restrict multi-airport connections",
        )
    )
    prefer_non_stop: bool = field(
        default="false",
        metadata=dict(
            name="PreferNonStop",
            type="Attribute",
            help="When non-stops are preferred, the distribution of search results should skew heavily toward non-stop flights while still returning some one stop flights for comparison and price competitiveness. The search request will ‘boost' the preference towards non-stops. If true then Non Stop flights will be preferred.",
        )
    )
    order_by: str = field(
        default=None,
        metadata=dict(
            name="OrderBy",
            type="Attribute",
            help="Indicates whether to sort by Journey Time, Deparature Time or Arrival Time. Applicable to air availability only.",
        )
    )
    exclude_open_jaw_airport: bool = field(
        default="false",
        metadata=dict(
            name="ExcludeOpenJawAirport",
            type="Attribute",
            help="This option ensures that travel into/out of each location will be into/out of the same airport of that location. Values are true or false. Default value is 'false'. If value is true then open jaws are exclude. If false the open jaws are included. The supported providers: 1P, 1J",
        )
    )
    exclude_ground_transportation: bool = field(
        default="false",
        metadata=dict(
            name="ExcludeGroundTransportation",
            type="Attribute",
            help="Indicates whether to allow the user to exclude ground transportation or not. Default value is 'false'. If value is true then ground transportations are excluded. If false then ground transportations are included. The supported providers: 1P, 1J",
        )
    )
    max_journey_time: TypeMaxJourneyTime = field(
        default=None,
        metadata=dict(
            name="MaxJourneyTime",
            type="Attribute",
            help="Maximum Journey Time for all legs (in hours) 0-99. For LFS Supported Providers are 1G,1V,1P,1J. For AirAvail Supported Providers are 1G,1V.",
        )
    )
    jet_service_only: bool = field(
        default=None,
        metadata=dict(
            name="JetServiceOnly",
            type="Attribute",
            help="Restricts results to Jet service flights only.",
        )
    )

    @dataclass
    class DisfavoredProviders:
        provider: List[Provider] = field(
            default_factory=list,
            metadata=dict(
                name="Provider",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredProviders:
        provider: List[Provider] = field(
            default_factory=list,
            metadata=dict(
                name="Provider",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class DisfavoredCarriers:
        carrier: List[Carrier] = field(
            default_factory=list,
            metadata=dict(
                name="Carrier",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PreferredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class DisfavoredAlliances:
        alliance: List[Alliance] = field(
            default_factory=list,
            metadata=dict(
                name="Alliance",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class PermittedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )

    @dataclass
    class ProhibitedBookingCodes:
        booking_code: List[BookingCode] = field(
            default_factory=list,
            metadata=dict(
                name="BookingCode",
                type="Element",
                help=None,
                min_occurs=1,
                max_occurs=999
            )
        )


@dataclass
class AirTicketingModifiers:
    """
    Modifiers used during ticketing
    """

    document_modifiers: DocumentModifiers = field(
        default=None,
        metadata=dict(
            name="DocumentModifiers",
            type="Element",
            help=None,
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tour_code: TourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element",
            help="Allows an agency to modify the tour code information during ticket issuance. Providers supported: Worldspan and JAL.",
        )
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            help="Allows an agency to add user defined ticketing endorsements in the ticket. Providers supported: Worldspan and JAL.",
            min_occurs=0,
            max_occurs=3
        )
    )
    commission: Commission = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            help="Allows an agency to add the commission to a new or different commission rate which will be applied at time of ticketing. The commission Modifier allows the user specify how the commission change is to applied. Providers supported: Worldspan and JAL.",
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="FormOfPayment information to be used as ticketing modifier at the time of ticketing. Providers supported: Galileo, Apollo, Worldspan and JAL.",
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            help="CreditCardAuth information to be used as ticketing modifier at the time of ticketing. Providers supported: Galileo, Apollo, Worldspan and JAL.",
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            help="Provide Payment for FOP. Providers supported: Galileo, Apollo, Worldspan and JAL.",
            min_occurs=0,
            max_occurs=999
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="The Plating Carrier used for this ticket",
        )
    )
    ticketed_fare_override: bool = field(
        default="false",
        metadata=dict(
            name="TicketedFareOverride",
            type="Attribute",
            help="It is a modifier to allow re-issuance of tickets for stored fares which are already ticketed. Providers supported are 1P/1J",
        )
    )
    suppress_tax_and_fee: bool = field(
        default="false",
        metadata=dict(
            name="SuppressTaxAndFee",
            type="Attribute",
            help="Allow to suppress Taxand Fee in ticketing response.Providers supported: Worldspan and JAL.",
        )
    )
    no_comparison_sfq: bool = field(
        default="false",
        metadata=dict(
            name="NoComparisonSFQ",
            type="Attribute",
            help="1P/1J - Set to 'true' to include the no comparison overide #NC to override the existing SFQ and issue the ticket. Only valid for AirTicketingReq, not valid for AirExchangeTicketingReq.",
        )
    )


@dataclass
class AlternateRoute:
    """
    Information about this Alternate Route component
    """

    leg: List[Leg] = field(
        default_factory=list,
        metadata=dict(
            name="Leg",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class ApisrequirementsList:
    """
    The shared object list of APISRequirements
    """

    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata=dict(
            name="APISRequirements",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class BaggageAllowance:
    """
    Free Baggage Allowance
    """

    number_of_pieces: int = field(
        default=None,
        metadata=dict(
            name="NumberOfPieces",
            type="Element",
            help=None,
        )
    )
    max_weight: TypeWeight = field(
        default=None,
        metadata=dict(
            name="MaxWeight",
            type="Element",
            help=None,
        )
    )


@dataclass
class BaggageRestriction:
    """
    Information related to Baggage restriction rules .
    """

    dimension: List[Dimension] = field(
        default_factory=list,
        metadata=dict(
            name="Dimension",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    max_weight: List[TypeUnitOfMeasure] = field(
        default_factory=list,
        metadata=dict(
            name="MaxWeight",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    text_info: List[TextInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TextInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class BookingRules:
    """
    Rules related to pre pay booking
    """

    booking_rules_fare_reference: List[BookingRulesFareReference] = field(
        default_factory=list,
        metadata=dict(
            name="BookingRulesFareReference",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rule_info: List["BookingRules.RuleInfo"] = field(
        default_factory=list,
        metadata=dict(
            name="RuleInfo",
            type="Element",
            help="Pre pay booking rule information",
            min_occurs=0,
            max_occurs=999
        )
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata=dict(
            name="Restriction",
            type="Element",
            help="Booking restrictions for associated pre pay account",
            min_occurs=0,
            max_occurs=999
        )
    )
    document_required: List[DocumentRequired] = field(
        default_factory=list,
        metadata=dict(
            name="DocumentRequired",
            type="Element",
            help="Detail about required documents for this pre pay id",
            min_occurs=0,
            max_occurs=999
        )
    )
    gender_dob_required: bool = field(
        default=None,
        metadata=dict(
            name="GenderDobRequired",
            type="Attribute",
            help="Vendor populates if gender/DOB data is required in book.",
        )
    )

    @dataclass
    class RuleInfo:
        charges_rules: ChargesRules = field(
            default=None,
            metadata=dict(
                name="ChargesRules",
                type="Element",
                help=None,
            )
        )


@dataclass
class BrandingInfo:
    """
    Branding information for the Ancillary Service. Returned in Seat Map only. Providers: 1G, 1V, 1P, 1J, ACH
    """

    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata=dict(
            name="PriceRange",
            type="Element",
            help="The price range of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
            min_occurs=0,
            max_occurs=5
        )
    )
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    title: List[Title] = field(
        default_factory=list,
        metadata=dict(
            name="Title",
            type="Element",
            help="The additional titles associated to the brand or optional service. Providers: ACH, 1G, 1V, 1P, 1J",
            min_occurs=0,
            max_occurs=2
        )
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata=dict(
            name="ImageLocation",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    service_group: ServiceGroup = field(
        default=None,
        metadata=dict(
            name="ServiceGroup",
            type="Element",
            help=None,
        )
    )
    air_segment_ref: List[TypeSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help="Specifies the AirSegment the branding information is for. Providers: ACH, 1G, 1V, 1P, 1J",
            min_occurs=1,
            max_occurs=99
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    service_sub_code: str = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            help="The Service Sub Code of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        )
    )
    external_service_name: str = field(
        default=None,
        metadata=dict(
            name="ExternalServiceName",
            type="Attribute",
            help="The external name of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        )
    )
    service_type: str = field(
        default=None,
        metadata=dict(
            name="ServiceType",
            type="Attribute",
            help="The type of Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
        )
    )
    commercial_name: str = field(
        default=None,
        metadata=dict(
            name="CommercialName",
            type="Attribute",
            help="The commercial name of the Ancillary Service. Providers: 1G, 1V, 1P, 1J, ACH",
            required=True
        )
    )
    chargeable: str = field(
        default=None,
        metadata=dict(
            name="Chargeable",
            type="Attribute",
            help="Indicates if the optional service is not offered, is available for a charge, or is included in the brand. Providers: 1G, 1V, 1P, 1J, ACH",
        )
    )


@dataclass
class BundledServices:
    bundled_service: List[BundledService] = field(
        default_factory=list,
        metadata=dict(
            name="BundledService",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=16
        )
    )


@dataclass
class Coupon(AttrElementKeyResults):
    """
    The flight coupon that resulted from the ticketing operation.
    """

    ticket_designator: List[TicketDesignator] = field(
        default_factory=list,
        metadata=dict(
            name="TicketDesignator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    coupon_number: int = field(
        default=None,
        metadata=dict(
            name="CouponNumber",
            type="Attribute",
            help="The sequential number of this coupon.",
        )
    )
    operating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="OperatingCarrier",
            type="Attribute",
            help="The true carrier.",
        )
    )
    operating_flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="OperatingFlightNumber",
            type="Attribute",
            help="The true carrier's flight number.",
        )
    )
    marketing_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="MarketingCarrier",
            type="Attribute",
            help="If codeshare applies to this, this is the marketing carrier (as opposed to the operating carrier).",
        )
    )
    marketing_flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="MarketingFlightNumber",
            type="Attribute",
            help="If codeshare applies to this, this is the marketing flight number (as opposed to the operating flight number).",
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Returns the airport or city code that defines the origin market for this fare.",
            required=True
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Returns the airport or city code that defines the destination market for this fare.",
            required=True
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="The date and time at which this entity departs. This does not include time zone information since it can be derived from the origin location. In case of open segment this will not be returned.",
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help="The date and time at which this entity arrives at the destination. This does not include time zone information since it can be derived from the origin location.",
        )
    )
    stopover_code: bool = field(
        default=None,
        metadata=dict(
            name="StopoverCode",
            type="Attribute",
            help="Stopover code - indicator that stopover is allowed at Origin Airport or City.",
            required=True
        )
    )
    booking_class: str = field(
        default=None,
        metadata=dict(
            name="BookingClass",
            type="Attribute",
            help="Booked fare class for coupon.",
            required=True,
            max_length=2.0
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help="The fare basis code for this fare",
            required=True
        )
    )
    not_valid_before: str = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute",
            help="Fare not valid before this date.",
        )
    )
    not_valid_after: str = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute",
            help="Fare not valid after this date.",
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="The status of this coupon returend from host is mapped as follows Code='A' Status='Airport Controlled' Code='C' Status='Checked In' Code='F' Status='Flown/Used' Code='L' Status='Boarded/Lifted' Code='O' Status='Open' Code='P' Status='Printed' Code='R' Status='Refunded' Code='E' Status='Exchanged' Code='V' Status='Void' Code='Z' Status='Archived/Carrier Modified' Code='U' Status='Unavailable' Code='S' Status='Suspended' Code='I' Status='Irregular Ops' Code='D' Status='Deleted/Removed' Code='X' Status='Unknown'",
            required=True,
            max_length=1.0
        )
    )
    segment_group: int = field(
        default=None,
        metadata=dict(
            name="SegmentGroup",
            type="Attribute",
            help="Indicates the grouping in which this segment resides based on Origin/Destination pairs in itinerary",
        )
    )
    marriage_group: int = field(
        default=None,
        metadata=dict(
            name="MarriageGroup",
            type="Attribute",
            help="Airline Marrraige group indicator",
        )
    )


@dataclass
class DetailedBillingInformation:
    """
    Container to send Detailed Billing Information for ticketing
    """

    form_of_payment_ref: FormOfPaymentRef = field(
        default=None,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            help=None,
        )
    )
    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help="Returns related air pricing infos.",
            min_occurs=1,
            max_occurs=999
        )
    )
    billing_detail_item: List[BillingDetailItem] = field(
        default_factory=list,
        metadata=dict(
            name="BillingDetailItem",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class DocumentInfo:
    """
    Container for the document information summary line.
    """

    ticket_info: List[TicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TicketInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    mcoinfo: List[Mcoinformation] = field(
        default_factory=list,
        metadata=dict(
            name="MCOInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrinfo: List[Tcrinfo] = field(
        default_factory=list,
        metadata=dict(
            name="TCRInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class DocumentSelect:
    """
    Allows an agency to select the documents to produce for the itinerary.
    """

    back_office_hand_off: BackOfficeHandOff = field(
        default=None,
        metadata=dict(
            name="BackOfficeHandOff",
            type="Element",
            help=None,
        )
    )
    itinerary: Itinerary = field(
        default=None,
        metadata=dict(
            name="Itinerary",
            type="Element",
            help=None,
        )
    )
    issue_ticket_only: bool = field(
        default=None,
        metadata=dict(
            name="IssueTicketOnly",
            type="Attribute",
            help="Set to true to alter system default of itinerary,ticket and back office.",
        )
    )
    issue_electronic_ticket: bool = field(
        default=None,
        metadata=dict(
            name="IssueElectronicTicket",
            type="Attribute",
            help="Set to true for electronic tickets.",
        )
    )
    fax_indicator: bool = field(
        default=None,
        metadata=dict(
            name="FaxIndicator",
            type="Attribute",
            help="Set to true for providing fax details.",
        )
    )


@dataclass
class ElectronicMiscDocument(AttrEmdsummary, AttrElementKeyResults):
    """
    Electronic miscellaneous document. Supported providers are 1G/1V/1P/1J
    """

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata=dict(
            name="EMDCoupon",
            type="Element",
            help="The coupon information for the EMD issued.",
            min_occurs=1,
            max_occurs=999
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="Status of the EMD calculated on the basis of coupon status. Possible values Open, Void, Refunded, Exchanged, Irregular Operations,Airport Control, Checked In, Flown/Used, Boarded/Lifted, Suspended, Unknown",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="System generated Key",
        )
    )


@dataclass
class EmbargoInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Embargo
    """

    pass


@dataclass
class Emdsummary(AttrEmdsummary, AttrElementKeyResults):
    """
    EMD summary information. Supported providers are 1G/1V/1P/1J
    """

    emdcoupon: List[Emdcoupon] = field(
        default_factory=list,
        metadata=dict(
            name="EMDCoupon",
            type="Element",
            help="The coupon information for the EMD issued.",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="System generated Key",
        )
    )


@dataclass
class Enumeration:
    """
    Provides the capability to group the results into differnt trip type and diversification strategies.
    """

    solution_group: List[SolutionGroup] = field(
        default_factory=list,
        metadata=dict(
            name="SolutionGroup",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class ExchangeEligibilityInfo:
    exchange_penalty_info: List[ExchangePenaltyInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangePenaltyInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    eligible_fares: str = field(
        default=None,
        metadata=dict(
            name="EligibleFares",
            type="Attribute",
            help="Identifies which fares are eligible for Exchange",
        )
    )
    refundable_fares: str = field(
        default=None,
        metadata=dict(
            name="RefundableFares",
            type="Attribute",
            help="Fares eligible for refund: All, Some, None",
        )
    )
    passed_automation_checks: bool = field(
        default=None,
        metadata=dict(
            name="PassedAutomationChecks",
            type="Attribute",
            help="Indicates whether the itinerary passed initial validation for automated exchange",
        )
    )


@dataclass
class ExpertSolution:
    """
    Information about Expert Solution Route component retrieved from Knowledge Base
    """

    leg_price: List[LegPrice] = field(
        default_factory=list,
        metadata=dict(
            name="LegPrice",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute",
            help="The Total Price for the Solution.",
        )
    )
    approximate_total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute",
            help="The Converted Total Price in Agency's Default Currency Value",
        )
    )
    created_date: str = field(
        default=None,
        metadata=dict(
            name="CreatedDate",
            type="Attribute",
            help="The Date on which this solution was created",
            required=True
        )
    )


@dataclass
class Facility:
    """
    The facility definition for a part of a row or a seat map
    """

    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata=dict(
            name="Characteristic",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    passenger_seat_price: List[PassengerSeatPrice] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerSeatPrice",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Tax information related to seat price. This is presently populated for MCH and ACH content. Applicable providers are MCH/ACH",
            min_occurs=0,
            max_occurs=999
        )
    )
    emd: Emd = field(
        default=None,
        metadata=dict(
            name="EMD",
            type="Element",
            help=None,
        )
    )
    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceData",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tour_code: TourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element",
            help=None,
        )
    )
    type: TypeFacility = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="The type of facility",
            required=True
        )
    )
    seat_code: str = field(
        default=None,
        metadata=dict(
            name="SeatCode",
            type="Attribute",
            help="If a seat type, the seat identifier",
        )
    )
    availability: TypeSeatAvailability = field(
        default=None,
        metadata=dict(
            name="Availability",
            type="Attribute",
            help="If a seat type, the availability of the seat",
        )
    )
    seat_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="SeatPrice",
            type="Attribute",
            help="The price of the seat, if applicable.",
        )
    )
    paid: bool = field(
        default=None,
        metadata=dict(
            name="Paid",
            type="Attribute",
            help="Set to True if either SeatPrice or GroupSeatPrice are returned.",
        )
    )
    service_sub_code: str = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            help="The service subcode associated with the Facility",
            max_length=3.0
        )
    )
    ssrcode: TypeSsrcode = field(
        default=None,
        metadata=dict(
            name="SSRCode",
            type="Attribute",
            help="The SSR Code associated with the Facility",
        )
    )
    issuance_reason: str = field(
        default=None,
        metadata=dict(
            name="IssuanceReason",
            type="Attribute",
            help="A one-letter RFIC value filed by the airline in each Optional Service will be mapped to this attribute. RFIC is IATA Reason for Issuance Code. Possible codes are A (Air transportation),B (Surface Transportation),C(Bagage), D(Financial Impact),E(Airport Services),F(Merchandise),G(Inflight Services),I (Individual Airline use).",
            min_length=1.0,
            max_length=1.0
        )
    )
    base_seat_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BaseSeatPrice",
            type="Attribute",
            help="Price of the seats excluding Taxes.",
        )
    )
    taxes: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help="Tax amount for the seat price.",
        )
    )
    quantity: int = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute",
            help="The number of units availed for each optional service (e.g. 2 baggage availed will be specified as 2 in quantity for optional service BAGGAGE)",
        )
    )
    sequence_number: int = field(
        default=None,
        metadata=dict(
            name="SequenceNumber",
            type="Attribute",
            help="The sequence number associated with the OptionalService",
        )
    )
    inclusive_of_tax: bool = field(
        default=None,
        metadata=dict(
            name="InclusiveOfTax",
            type="Attribute",
            help="Identifies if the service was filed with a fee that is inclusive of tax.",
        )
    )
    interline_settlement_allowed: bool = field(
        default=None,
        metadata=dict(
            name="InterlineSettlementAllowed",
            type="Attribute",
            help="Identifies if the interline settlement is allowed in service .",
        )
    )
    geography_specification: str = field(
        default=None,
        metadata=dict(
            name="GeographySpecification",
            type="Attribute",
            help="Sector, Portion, Journey.",
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            help="The Source of the optional service. The source can be ACH, MCE, or MCH.",
        )
    )
    optional_service_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="OptionalServiceRef",
            type="Attribute",
            help="References the OptionalService for the Row/Facility. Providers: ACH, 1G, 1V, 1P, 1J",
        )
    )
    seat_information_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SeatInformationRef",
            type="Attribute",
            help="Specifies the seat information for the seat. Providers: ACH, 1G, 1V, 1P, 1J",
        )
    )


@dataclass
class FareDetails:
    """
    Information about this fare component
    """

    fare_ticket_designator: FareTicketDesignator = field(
        default=None,
        metadata=dict(
            name="FareTicketDesignator",
            type="Element",
            help=None,
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Fare key",
            required=True
        )
    )
    passenger_detail_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="PassengerDetailRef",
            type="Attribute",
            help="PassengerRef key",
            required=True
        )
    )
    fare_basis: TypeFareBasisCode = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help="The fare basis code for this fare",
            required=True
        )
    )


@dataclass
class FareRemarkList:
    """
    The shared object list of FareInfos
    """

    fare_remark: List[FareRemark] = field(
        default_factory=list,
        metadata=dict(
            name="FareRemark",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareRestriction:
    """
    Fare Restriction
    """

    fare_restriction_days_of_week: List[FareRestrictionDaysOfWeek] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictionDaysOfWeek",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=3
        )
    )
    fare_restriction_date: List[FareRestrictionDate] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictionDate",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_restriction_sale_date: FareRestrictionSaleDate = field(
        default=None,
        metadata=dict(
            name="FareRestrictionSaleDate",
            type="Element",
            help=None,
        )
    )
    fare_restriction_seasonal: List[FareRestrictionSeasonal] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestrictionSeasonal",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_restrictiontype: TypeFareRestrictionType = field(
        default=None,
        metadata=dict(
            name="FareRestrictiontype",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareRuleCategoryTypes:
    category_details: List[ValueDetails] = field(
        default_factory=list,
        metadata=dict(
            name="CategoryDetails",
            type="Element",
            help="To indicate details of which category is displayed",
            min_occurs=0,
            max_occurs=99
        )
    )
    variable_category_details: List[CategoryDetailsType] = field(
        default_factory=list,
        metadata=dict(
            name="VariableCategoryDetails",
            type="Element",
            help="If the specified category of Structured Fare Rules is of variable lenght",
            min_occurs=0,
            max_occurs=99
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class FareRulesFilter:
    """
    Fare Rules Filter about this fare component. Applicable Providers are 1P,1J,1G,1V.
    """

    refundability: "FareRulesFilter.Refundability" = field(
        default=None,
        metadata=dict(
            name="Refundability",
            type="Element",
            help="Refundability/Penalty Fare Rules about this fare component.",
        )
    )
    latest_ticketing_time: str = field(
        default=None,
        metadata=dict(
            name="LatestTicketingTime",
            type="Element",
            help="For Future Use",
        )
    )
    chg: Chgtype = field(
        default=None,
        metadata=dict(
            name="CHG",
            type="Element",
            help="For Penalties",
        )
    )
    min: Mintype = field(
        default=None,
        metadata=dict(
            name="MIN",
            type="Element",
            help="For Minimum Stay",
        )
    )
    max: Maxtype = field(
        default=None,
        metadata=dict(
            name="MAX",
            type="Element",
            help="For Maximum Stay",
        )
    )
    adv: Advtype = field(
        default=None,
        metadata=dict(
            name="ADV",
            type="Element",
            help="For Advance Res/Tkt",
        )
    )
    oth: Othtype = field(
        default=None,
        metadata=dict(
            name="OTH",
            type="Element",
            help="Other",
        )
    )

    @dataclass
    class Refundability:
        value: TypeRefundabilityValue = field(
            default=None,
            metadata=dict(
                name="Value",
                type="Attribute",
                help="Currently returned: FullyRefundable (1G,1V), RefundableWithPenalty (1G,1V), Refundable (1P,1J), NonRefundable (1G,1V,1P,1J).Refundable.",
                required=True
            )
        )


@dataclass
class FaxDetails:
    """
    The Fax Details Information
    """

    phone_number: PhoneNumber = field(
        default=None,
        metadata=dict(
            name="PhoneNumber",
            type="Element",
            help="Send type as Fax for fax number.",
            required=True
        )
    )
    term_conditions: TermConditions = field(
        default=None,
        metadata=dict(
            name="TermConditions",
            type="Element",
            help="Term and Conditions for the fax .",
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    include_cover_sheet: bool = field(
        default=None,
        metadata=dict(
            name="IncludeCoverSheet",
            type="Attribute",
            help="Specifies whether to include a cover page with fax or not.",
        )
    )
    to: str = field(
        default=None,
        metadata=dict(
            name="To",
            type="Attribute",
            help="To address.",
        )
    )
    from_value: str = field(
        default=None,
        metadata=dict(
            name="From",
            type="Attribute",
            help="From address.",
        )
    )
    dept_billing_code: str = field(
        default=None,
        metadata=dict(
            name="DeptBillingCode",
            type="Attribute",
            help="Department billing code.",
        )
    )
    invoice_number: str = field(
        default=None,
        metadata=dict(
            name="InvoiceNumber",
            type="Attribute",
            help="Invoice number.",
        )
    )


@dataclass
class FlightDetails(AttrOrigDestDepatureInfo, AttrFlightTimes, AttrElementKeyResults):
    """
    Specific details within a flight segment.
    """

    connection: Connection = field(
        default=None,
        metadata=dict(
            name="Connection",
            type="Element",
            help=None,
        )
    )
    meals: List[Meals] = field(
        default_factory=list,
        metadata=dict(
            name="Meals",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    in_flight_services: List[InFlightServices] = field(
        default_factory=list,
        metadata=dict(
            name="InFlightServices",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    equipment: TypeEquipment = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            help=None,
        )
    )
    on_time_performance: int = field(
        default=None,
        metadata=dict(
            name="OnTimePerformance",
            type="Attribute",
            help="Represents flight on time performance as a percentage from 0 to 100",
        )
    )
    origin_terminal: str = field(
        default=None,
        metadata=dict(
            name="OriginTerminal",
            type="Attribute",
            help=None,
        )
    )
    destination_terminal: str = field(
        default=None,
        metadata=dict(
            name="DestinationTerminal",
            type="Attribute",
            help=None,
        )
    )
    ground_time: int = field(
        default=None,
        metadata=dict(
            name="GroundTime",
            type="Attribute",
            help=None,
        )
    )
    automated_checkin: bool = field(
        default="false",
        metadata=dict(
            name="AutomatedCheckin",
            type="Attribute",
            help="“True” indicates that the flight allows automated check-in. The default is “False”.",
        )
    )


@dataclass
class FlightInfoDetail:
    codeshare_info: CodeshareInfo = field(
        default=None,
        metadata=dict(
            name="CodeshareInfo",
            type="Element",
            help=None,
        )
    )
    meals: List[Meals] = field(
        default_factory=list,
        metadata=dict(
            name="Meals",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    in_flight_services: List[InFlightServices] = field(
        default_factory=list,
        metadata=dict(
            name="InFlightServices",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    variance: List[Variance] = field(
        default_factory=list,
        metadata=dict(
            name="Variance",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
            required=True
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
            required=True
        )
    )
    scheduled_departure_time: str = field(
        default=None,
        metadata=dict(
            name="ScheduledDepartureTime",
            type="Attribute",
            help="The date and time at which this entity is scheduled to depart. This does not include time zone information since it can be derived from the origin location.",
        )
    )
    scheduled_arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ScheduledArrivalTime",
            type="Attribute",
            help="The date and time at which this entity is scheduled to arrive at the destination. This does not include time zone information since it can be derived from the origin location.",
        )
    )
    travel_time: int = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute",
            help="Total time spent (minutes) traveling including flight time and ground time.",
        )
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute",
            help="Identifies if this particular segment is E-Ticketable",
        )
    )
    equipment: TypeEquipment = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            help=None,
        )
    )
    origin_terminal: str = field(
        default=None,
        metadata=dict(
            name="OriginTerminal",
            type="Attribute",
            help=None,
        )
    )
    origin_gate: str = field(
        default=None,
        metadata=dict(
            name="OriginGate",
            type="Attribute",
            help="To be used to display origin flight gate number",
            max_length=6.0
        )
    )
    destination_terminal: str = field(
        default=None,
        metadata=dict(
            name="DestinationTerminal",
            type="Attribute",
            help=None,
        )
    )
    destination_gate: str = field(
        default=None,
        metadata=dict(
            name="DestinationGate",
            type="Attribute",
            help="To be used to display destination flight gate number",
            max_length=6.0
        )
    )
    automated_checkin: bool = field(
        default="false",
        metadata=dict(
            name="AutomatedCheckin",
            type="Attribute",
            help="“True” indicates that the flight allows automated check-in. The default is “False”.",
        )
    )


@dataclass
class FlightTimeDetail:
    """
    Flight Time Table Response Details
    """

    days_of_operation: TypeDaysOfOperation = field(
        default=None,
        metadata=dict(
            name="DaysOfOperation",
            type="Element",
            help=None,
        )
    )
    connection: Connection = field(
        default=None,
        metadata=dict(
            name="Connection",
            type="Element",
            help=None,
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    vendor_code: str = field(
        default=None,
        metadata=dict(
            name="VendorCode",
            type="Attribute",
            help=None,
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help=None,
        )
    )
    origin: TypeAirport = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help=None,
        )
    )
    destination: TypeAirport = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help=None,
        )
    )
    departure_time: str = field(
        default=None,
        metadata=dict(
            name="DepartureTime",
            type="Attribute",
            help="Flight departure time",
        )
    )
    arrival_time: str = field(
        default=None,
        metadata=dict(
            name="ArrivalTime",
            type="Attribute",
            help="Flight arrival time",
        )
    )
    stop_count: int = field(
        default=None,
        metadata=dict(
            name="StopCount",
            type="Attribute",
            help=None,
        )
    )
    equipment: TypeEquipment = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            help=None,
        )
    )
    schedule_start_date: str = field(
        default=None,
        metadata=dict(
            name="ScheduleStartDate",
            type="Attribute",
            help="Flight time table search start date",
        )
    )
    schedule_end_date: str = field(
        default=None,
        metadata=dict(
            name="ScheduleEndDate",
            type="Attribute",
            help="Flight time table search end date",
        )
    )
    display_option: bool = field(
        default=None,
        metadata=dict(
            name="DisplayOption",
            type="Attribute",
            help="Indicates if carrier has link (carrier specific) display option.",
        )
    )
    on_time_performance: int = field(
        default=None,
        metadata=dict(
            name="OnTimePerformance",
            type="Attribute",
            help="On time performance indicator in percentage.",
        )
    )
    day_change: int = field(
        default=None,
        metadata=dict(
            name="DayChange",
            type="Attribute",
            help="Indicates if flight arrives on same day as departure, previous day, or next day. Like values 00 means Same day , 01 means next day, -1 mean Previous day etc.",
        )
    )
    journey_time: int = field(
        default=None,
        metadata=dict(
            name="JourneyTime",
            type="Attribute",
            help="Indicates total journey time in minutes.",
        )
    )
    flight_time: int = field(
        default=None,
        metadata=dict(
            name="FlightTime",
            type="Attribute",
            help="Indicates total flight time in minutes.",
        )
    )
    start_terminal: str = field(
        default=None,
        metadata=dict(
            name="StartTerminal",
            type="Attribute",
            help="Flight start terminal code.",
        )
    )
    end_terminal: str = field(
        default=None,
        metadata=dict(
            name="EndTerminal",
            type="Attribute",
            help="Flight end terminal code.",
        )
    )
    first_intermediate_stop: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="FirstIntermediateStop",
            type="Attribute",
            help="First intermediate stop after board point.",
        )
    )
    last_intermediate_stop: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="LastIntermediateStop",
            type="Attribute",
            help="Last intermediate stop before off point.",
        )
    )
    inside_availability: str = field(
        default=None,
        metadata=dict(
            name="InsideAvailability",
            type="Attribute",
            help=None,
            min_length=1.0,
            max_length=1.0
        )
    )
    secure_sell: str = field(
        default=None,
        metadata=dict(
            name="SecureSell",
            type="Attribute",
            help=None,
            min_length=0.0,
            max_length=2.0
        )
    )
    availability_source: TypeAvailabilitySource = field(
        default=None,
        metadata=dict(
            name="AvailabilitySource",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class GeneralTimeTable:
    days_of_operation: TypeDaysOfOperation = field(
        default=None,
        metadata=dict(
            name="DaysOfOperation",
            type="Element",
            help=None,
        )
    )
    flight_origin: TypeLocation = field(
        default=None,
        metadata=dict(
            name="FlightOrigin",
            type="Element",
            help=None,
            required=True
        )
    )
    flight_destination: TypeLocation = field(
        default=None,
        metadata=dict(
            name="FlightDestination",
            type="Element",
            help=None,
            required=True
        )
    )
    carrier_list: CarrierList = field(
        default=None,
        metadata=dict(
            name="CarrierList",
            type="Element",
            help=None,
        )
    )
    start_date: str = field(
        default=None,
        metadata=dict(
            name="StartDate",
            type="Attribute",
            help=None,
            required=True
        )
    )
    end_date: str = field(
        default=None,
        metadata=dict(
            name="EndDate",
            type="Attribute",
            help=None,
        )
    )
    start_time: str = field(
        default=None,
        metadata=dict(
            name="StartTime",
            type="Attribute",
            help="Flight start time of flight time tabel .",
        )
    )
    end_time: str = field(
        default=None,
        metadata=dict(
            name="EndTime",
            type="Attribute",
            help="Flight end time of flight time tabel .",
        )
    )
    include_connection: bool = field(
        default=None,
        metadata=dict(
            name="IncludeConnection",
            type="Attribute",
            help="Include or exclude connecting flights.",
        )
    )


@dataclass
class Option:
    """
    List of segment and fare available for the search air leg.
    """

    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BookingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata=dict(
            name="Connection",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    travel_time: str = field(
        default=None,
        metadata=dict(
            name="TravelTime",
            type="Attribute",
            help="Total traveling time that is difference between the departure time of the first segment and the arrival time of the last segments for that particular entire set of connection.",
        )
    )


@dataclass
class PassengerType(TypePassengerType):
    """
    The passenger type details associated to a fare.
    """

    fare_guarantee_info: FareGuaranteeInfo = field(
        default=None,
        metadata=dict(
            name="FareGuaranteeInfo",
            type="Element",
            help=None,
        )
    )


@dataclass
class PrePayAccount:
    """
    PrePay Account associated with the customer
    """

    credit_summary: CreditSummary = field(
        default=None,
        metadata=dict(
            name="CreditSummary",
            type="Element",
            help=None,
        )
    )
    pre_pay_price_info: PrePayPriceInfo = field(
        default=None,
        metadata=dict(
            name="PrePayPriceInfo",
            type="Element",
            help=None,
        )
    )
    program_title: str = field(
        default=None,
        metadata=dict(
            name="ProgramTitle",
            type="Attribute",
            help="Pre pay program title",
        )
    )
    certificate_number: str = field(
        default=None,
        metadata=dict(
            name="CertificateNumber",
            type="Attribute",
            help=None,
        )
    )
    program_name: str = field(
        default=None,
        metadata=dict(
            name="ProgramName",
            type="Attribute",
            help="Pre pay program name",
        )
    )
    effective_date: str = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute",
            help="Effective date for the pre pay account",
        )
    )
    expire_date: str = field(
        default=None,
        metadata=dict(
            name="ExpireDate",
            type="Attribute",
            help="Expiry date for the pre pay account",
        )
    )


@dataclass
class PrePayCustomer:
    """
    Detailed customer information for searching pre pay profiles
    """

    person_name: PersonName = field(
        default=None,
        metadata=dict(
            name="PersonName",
            type="Element",
            help=None,
        )
    )
    email: List[Email] = field(
        default_factory=list,
        metadata=dict(
            name="Email",
            type="Element",
            help="Customer email detail",
            min_occurs=0,
            max_occurs=999
        )
    )
    address: List[TypeStructuredAddress] = field(
        default_factory=list,
        metadata=dict(
            name="Address",
            type="Element",
            help="Customer address detail",
            min_occurs=0,
            max_occurs=999
        )
    )
    related_traveler: List[RelatedTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="RelatedTraveler",
            type="Element",
            help="Travelers related to this pre pay id",
            min_occurs=0,
            max_occurs=999
        )
    )
    loyalty_card: List[LoyaltyCard] = field(
        default_factory=list,
        metadata=dict(
            name="LoyaltyCard",
            type="Element",
            help="Customer loyalty card detail",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class RepricingModifiers:
    """
    Used for rapid reprice to provide additional options for the reprice. Providers: 1G/1V/1P/1S/1A
    """

    private_fare_options: str = field(
        default=None,
        metadata=dict(
            name="PrivateFareOptions",
            type="Element",
            help="Public and/or Private Fares requested for pricing. Currently supported: AccountCodeOnly, PrivateFaresOnly, PublicPrivateFaresOnly.",
            max_length=50.0
        )
    )
    fare_type: List[FareType] = field(
        default_factory=list,
        metadata=dict(
            name="FareType",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=100
        )
    )
    fare_ticket_designator: FareTicketDesignator = field(
        default=None,
        metadata=dict(
            name="FareTicketDesignator",
            type="Element",
            help=None,
        )
    )
    override_currency: "RepricingModifiers.OverrideCurrency" = field(
        default=None,
        metadata=dict(
            name="OverrideCurrency",
            type="Element",
            help=None,
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    withhold_tax_code: List[str] = field(
        default_factory=list,
        metadata=dict(
            name="WithholdTaxCode",
            type="Element",
            help="Used to request tax withholding for the tax code specified. Providers supported 1G/1P",
            min_occurs=0,
            max_occurs=4,
            length=2
        )
    )
    price_class_of_service: TypePriceClassOfService = field(
        default=None,
        metadata=dict(
            name="PriceClassOfService",
            type="Attribute",
            help="Values allowed are ClassBooked or LowestClass. This tells how to price the new itinerary.",
        )
    )
    create_date: str = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute",
            help="This is either today’s date or the date the repriced itinerary was created",
        )
    )
    reissue_loc_city_code: TypeCity = field(
        default=None,
        metadata=dict(
            name="ReissueLocCityCode",
            type="Attribute",
            help="This is the city code of the reissue location",
        )
    )
    reissue_loc_country_code: TypeCountry = field(
        default=None,
        metadata=dict(
            name="ReissueLocCountryCode",
            type="Attribute",
            help="This is the country code of the reissue location",
        )
    )
    bulk_ticket: bool = field(
        default="false",
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Set to true and the itinerary is/will be a bulk ticket. Set to false and the itinerary being repriced will not be a bulk ticket.",
        )
    )
    account_code: str = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Attribute",
            help="May be used in conjunction with PrivateFareOptions",
        )
    )
    penalty_as_tax_code: str = field(
        default=None,
        metadata=dict(
            name="PenaltyAsTaxCode",
            type="Attribute",
            help="Used to request that the penalty be applied as a tax, to the tax code specified. Providers supported 1G/1P",
            length=2
        )
    )
    air_pricing_solution_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirPricingSolutionRef",
            type="Attribute",
            help="A reference to a AirPricingSolution. Providers: 1G, 1V, 1P, 1J.",
        )
    )
    penalty_to_fare: bool = field(
        default=None,
        metadata=dict(
            name="PenaltyToFare",
            type="Attribute",
            help="Will add the change fee/penalty amount to the total fare amount. Supported Providers: 1P",
        )
    )
    price_ptconly: bool = field(
        default="false",
        metadata=dict(
            name="PricePTCOnly",
            type="Attribute",
            help="A value of true forces the price for the PTC even if that fare is not the lowest fare for the passenger.",
        )
    )
    brand_details: bool = field(
        default="false",
        metadata=dict(
            name="BrandDetails",
            type="Attribute",
            help="Set to true full brand details will be returned.",
        )
    )
    brand_modifier: str = field(
        default=None,
        metadata=dict(
            name="BrandModifier",
            type="Attribute",
            help="A value of MaintainBrand will maintain the brand from the original ticket if applicable.",
        )
    )
    jet_service_only: bool = field(
        default="false",
        metadata=dict(
            name="JetServiceOnly",
            type="Attribute",
            help="Request flights that are jet service only. Available in AirExchangeMultiQuoteReq only.",
        )
    )
    time_window: int = field(
        default=None,
        metadata=dict(
            name="TimeWindow",
            type="Attribute",
            help="A value of Time Window is optional. Available in AirExchangeMultiQuoteReq only.",
            min_inclusive=1.0,
            max_inclusive=12.0
        )
    )
    flight_type: str = field(
        default="Direct",
        metadata=dict(
            name="FlightType",
            type="Attribute",
            help="Type of flights to be returned. Values are 'NonStop', 'Direct', 'SingleConnection' and 'NoRestrictions'. Available in AirExchangeMultiQuoteReq only.",
        )
    )
    multi_airport_search: bool = field(
        default="true",
        metadata=dict(
            name="MultiAirportSearch",
            type="Attribute",
            help="A value of Multi Airport Search Indicator is optional. Available in AirExchangeMultiQuoteReq only.",
        )
    )
    connection_point: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="ConnectionPoint",
            type="Attribute",
            help="A value of Connection City Code is optional. Available in AirExchangeMultiQuoteReq only.",
        )
    )

    @dataclass
    class OverrideCurrency:
        currency_code: TypeCurrency = field(
            default=None,
            metadata=dict(
                name="CurrencyCode",
                type="Attribute",
                help=None,
            )
        )
        country_code: TypeCountry = field(
            default=None,
            metadata=dict(
                name="CountryCode",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class Route:
    """
    Information about this Route component
    """

    leg: List[Leg] = field(
        default_factory=list,
        metadata=dict(
            name="Leg",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class RuleLengthOfStay:
    """
    Container for rules providing minimum and maximum stay requirements.
    """

    minimum_stay: TypeRestrictionLengthOfStay = field(
        default=None,
        metadata=dict(
            name="MinimumStay",
            type="Element",
            help=None,
        )
    )
    maximum_stay: TypeRestrictionLengthOfStay = field(
        default=None,
        metadata=dict(
            name="MaximumStay",
            type="Element",
            help=None,
        )
    )


@dataclass
class ServiceAssociations:
    applicable_segment: List["ServiceAssociations.ApplicableSegment"] = field(
        default_factory=list,
        metadata=dict(
            name="ApplicableSegment",
            type="Element",
            help="Applicable air segment associated with this brand.",
            min_occurs=1,
            max_occurs=999
        )
    )

    @dataclass
    class ApplicableSegment:
        response_message: ResponseMessage = field(
            default=None,
            metadata=dict(
                name="ResponseMessage",
                type="Element",
                help=None,
            )
        )
        optional_service_ref: OptionalServiceRef = field(
            default=None,
            metadata=dict(
                name="OptionalServiceRef",
                type="Element",
                help=None,
            )
        )
        key: TypeRef = field(
            default=None,
            metadata=dict(
                name="Key",
                type="Attribute",
                help="Applicable air segment key",
            )
        )


@dataclass
class TypeDefaultBrandDetail:
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help="Text associated to the brand",
            min_occurs=0,
            max_occurs=4
        )
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata=dict(
            name="ImageLocation",
            type="Element",
            help="Images associated to the brand",
            min_occurs=0,
            max_occurs=3
        )
    )
    applicable_segment: List[ApplicableSegment] = field(
        default_factory=list,
        metadata=dict(
            name="ApplicableSegment",
            type="Element",
            help="Defines for which air segment the brand is applicable.",
            min_occurs=0,
            max_occurs=99
        )
    )
    brand_id: TypeBrandId = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            help="The unique identifier of the brand",
        )
    )


@dataclass
class AccountRelatedRules:
    booking_rules: List[BookingRules] = field(
        default_factory=list,
        metadata=dict(
            name="BookingRules",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    routing_rules: RoutingRules = field(
        default=None,
        metadata=dict(
            name="RoutingRules",
            type="Element",
            help=None,
        )
    )


@dataclass
class AirPricingCommand:
    """
    A containter to identify individual pricing events. A pricing result will be returned for each pricing command according to its parameters.
    """

    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            help=None,
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    command_key: str = field(
        default=None,
        metadata=dict(
            name="CommandKey",
            type="Attribute",
            help="An identifier to link the pricing responses to the pricing commands. The value passed here will be returned in the resulting AirPricingInfo(s) from this command.",
            max_length=10.0
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="Specify the cabin type to price the entire itinerary in. If segment level cabin selection is required, this attribute should not be used.",
        )
    )


@dataclass
class AlternateRouteList:
    """
    Identifies the alternate routes for the request
    """

    alternate_route: List[AlternateRoute] = field(
        default_factory=list,
        metadata=dict(
            name="AlternateRoute",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AutoPricingInfo(AttrElementKeyResults):
    """
    Auto Pricing based on Segment and Traveler Association.
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=100
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=100
        )
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            help=None,
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=100
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    pricing_type: str = field(
        default=None,
        metadata=dict(
            name="PricingType",
            type="Attribute",
            help="Indicates the Pricing Type used. The possible values are TicketRecord, StoredFare, PricingInstruction.",
            max_length=25.0
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="The Plating Carrier for this journey",
        )
    )


@dataclass
class BagDetails:
    """
    Information related to Bag details .
    """

    baggage_restriction: List[BaggageRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageRestriction",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    available_discount: List[AvailableDiscount] = field(
        default_factory=list,
        metadata=dict(
            name="AvailableDiscount",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    applicable_bags: str = field(
        default=None,
        metadata=dict(
            name="ApplicableBags",
            type="Attribute",
            help="Applicable baggage like Carry-On,1st Check-in,2nd Check -in etc.",
            required=True
        )
    )
    base_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute",
            help=None,
        )
    )
    approximate_base_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateBasePrice",
            type="Attribute",
            help=None,
        )
    )
    taxes: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help=None,
        )
    )
    total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalPrice",
            type="Attribute",
            help=None,
        )
    )
    approximate_total_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ApproximateTotalPrice",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class CarryOnAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Carry-On allowance like URL, pricing etc
    """

    carry_on_details: List["CarryOnAllowanceInfo.CarryOnDetails"] = field(
        default_factory=list,
        metadata=dict(
            name="CarryOnDetails",
            type="Element",
            help="Information related to Carry-On Bag details .",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class CarryOnDetails:
        baggage_restriction: List[BaggageRestriction] = field(
            default_factory=list,
            metadata=dict(
                name="BaggageRestriction",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=99
            )
        )
        applicable_carry_on_bags: str = field(
            default=None,
            metadata=dict(
                name="ApplicableCarryOnBags",
                type="Attribute",
                help="Applicable Carry-On baggage 'First', 'Second', 'Third' etc",
            )
        )
        base_price: TypeMoney = field(
            default=None,
            metadata=dict(
                name="BasePrice",
                type="Attribute",
                help=None,
            )
        )
        approximate_base_price: TypeMoney = field(
            default=None,
            metadata=dict(
                name="ApproximateBasePrice",
                type="Attribute",
                help=None,
            )
        )
        taxes: TypeMoney = field(
            default=None,
            metadata=dict(
                name="Taxes",
                type="Attribute",
                help=None,
            )
        )
        total_price: TypeMoney = field(
            default=None,
            metadata=dict(
                name="TotalPrice",
                type="Attribute",
                help=None,
            )
        )
        approximate_total_price: TypeMoney = field(
            default=None,
            metadata=dict(
                name="ApproximateTotalPrice",
                type="Attribute",
                help=None,
            )
        )


@dataclass
class DefaultBrandDetail(TypeDefaultBrandDetail):
    """
    Applicable air segment.
    """

    pass


@dataclass
class Emdinfo(ProviderReservation, AttrElementKeyResults):
    """
    This is the parent container to display EMD information. Occurrence of multiple unique EMDs inside this container indicate that those EMDs are conjunctive to each other. Supported providers are 1G/1V/1P/1J
    """

    emdtraveler_info: EmdtravelerInfo = field(
        default=None,
        metadata=dict(
            name="EMDTravelerInfo",
            type="Element",
            help="Basic information of the traveler associated with this EMDInfo.",
            required=True
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            help="List of Supplier Locator information that is associated with this document",
            min_occurs=0,
            max_occurs=999
        )
    )
    electronic_misc_document: List[ElectronicMiscDocument] = field(
        default_factory=list,
        metadata=dict(
            name="ElectronicMiscDocument",
            type="Element",
            help="Electronic miscellaneous documents.As an EMDInfo container displays all the EMDs which are in conjunction, there can be maximum 4 ElectronicMiscDocuments present in an EMDInfo",
            min_occurs=1,
            max_occurs=999
        )
    )
    payment: Payment = field(
        default=None,
        metadata=dict(
            name="Payment",
            type="Element",
            help="Payment charged for EMD isuance",
        )
    )
    form_of_payment: FormOfPayment = field(
        default=None,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help="FormOfPayment used for issuing these electronic miscellaneous documents",
        )
    )
    emdpricing_info: EmdpricingInfo = field(
        default=None,
        metadata=dict(
            name="EMDPricingInfo",
            type="Element",
            help="Fare related information for these electronic miscellaneous documents",
        )
    )
    emdendorsement: List[Emdendorsement] = field(
        default_factory=list,
        metadata=dict(
            name="EMDEndorsement",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_calc: FareCalc = field(
        default=None,
        metadata=dict(
            name="FareCalc",
            type="Element",
            help="Infomration about the fare calculation",
        )
    )
    emdcommission: Emdcommission = field(
        default=None,
        metadata=dict(
            name="EMDCommission",
            type="Element",
            help="Commission information applied during EMD issuance",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="System generated Key",
        )
    )


@dataclass
class EmdsummaryInfo(AttrElementKeyResults):
    """
    Container for EMD summary information. Supported providers are 1G/1V/1P/1J
    """

    emdsummary: List[Emdsummary] = field(
        default_factory=list,
        metadata=dict(
            name="EMDSummary",
            type="Element",
            help="Summary information for EMDs conjuncted to each other.",
            min_occurs=1,
            max_occurs=999
        )
    )
    emdtraveler_info: EmdtravelerInfo = field(
        default=None,
        metadata=dict(
            name="EMDTravelerInfo",
            type="Element",
            help="EMD traveler information.",
            required=True
        )
    )
    payment: Payment = field(
        default=None,
        metadata=dict(
            name="Payment",
            type="Element",
            help="Payment charged to issue EMD.",
        )
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="A reference to the provider reservation with which the document is associated.Displayed when shown as part of UR.Not displayed in EMDRetrieveRsp",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="System generated Key",
        )
    )


@dataclass
class ExpertSolutionList:
    """
    Identifies the Expert Solutions retrieved from the Knowledge Base.
    """

    expert_solution: List[ExpertSolution] = field(
        default_factory=list,
        metadata=dict(
            name="ExpertSolution",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareDisplayRule:
    """
    Fare Display Rule Container
    """

    rule_advanced_purchase: RuleAdvancedPurchase = field(
        default=None,
        metadata=dict(
            name="RuleAdvancedPurchase",
            type="Element",
            help=None,
        )
    )
    rule_length_of_stay: RuleLengthOfStay = field(
        default=None,
        metadata=dict(
            name="RuleLengthOfStay",
            type="Element",
            help=None,
        )
    )
    rule_charges: RuleCharges = field(
        default=None,
        metadata=dict(
            name="RuleCharges",
            type="Element",
            help=None,
        )
    )
    rule_number: str = field(
        default=None,
        metadata=dict(
            name="RuleNumber",
            type="Attribute",
            help=None,
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            help=None,
        )
    )
    tariff_number: str = field(
        default=None,
        metadata=dict(
            name="TariffNumber",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FaxDetailsInformation:
    """
    Container to send Fax details Information for ticketing
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help="Returns related air pricing infos.",
            min_occurs=1,
            max_occurs=999
        )
    )
    fax_details: FaxDetails = field(
        default=None,
        metadata=dict(
            name="FaxDetails",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class FlightDetailsList:
    """
    The shared object list of FlightDetails
    """

    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata=dict(
            name="FlightDetails",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FlightInfo:
    flight_info_detail: List[FlightInfoDetail] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoDetail",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_info_error_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="FlightInfoErrorMessage",
            type="Element",
            help="Errors, Warnings and informational messages for the Flight referenced above.",
            min_occurs=0,
            max_occurs=999
        )
    )
    criteria_key: TypeRef = field(
        default=None,
        metadata=dict(
            name="CriteriaKey",
            type="Attribute",
            help="An identifier to link the flightinfo responses to the criteria in request. The value populated here is passed in request.",
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="The carrier that is marketing this segment",
            required=True
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="The flight number under which the marketing carrier is marketing this flight",
            required=True
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
        )
    )
    departure_date: str = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            help="The date at which this entity departs. This does not include time zone information since it can be derived from the origin location.",
            required=True
        )
    )
    class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FlightOption:
    """
    List of Options available for any search air leg.
    """

    option: List[Option] = field(
        default_factory=list,
        metadata=dict(
            name="Option",
            type="Element",
            help="List of BookingInfo available for the search air leg.",
            min_occurs=1,
            max_occurs=999
        )
    )
    leg_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="LegRef",
            type="Attribute",
            help="Identifies the Leg Reference for this Flight Option.",
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
            required=True
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
            required=True
        )
    )


@dataclass
class FlightTimeTableCriteria:
    """
    Flight Time Table Search Criteria
    """

    general_time_table: GeneralTimeTable = field(
        default=None,
        metadata=dict(
            name="GeneralTimeTable",
            type="Element",
            help=None,
            required=True
        )
    )
    specific_time_table: SpecificTimeTable = field(
        default=None,
        metadata=dict(
            name="SpecificTimeTable",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class MerchandisingAvailabilityDetails:
    """
    Rich Content and Branding for an air segment
    """

    air_itinerary_details: AirItineraryDetails = field(
        default=None,
        metadata=dict(
            name="AirItineraryDetails",
            type="Element",
            help=None,
            required=True
        )
    )
    account_code: AccountCode = field(
        default=None,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help=None,
        )
    )


@dataclass
class MerchandisingDetails:
    """
    Rich Content and Branding for a fare brand.
    """

    air_itinerary_details: List[AirItineraryDetails] = field(
        default_factory=list,
        metadata=dict(
            name="AirItineraryDetails",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=99
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=10
        )
    )


@dataclass
class OptionalService(AttrProviderSupplier, AttrPrices, AttrElementKeyResults):
    service_data: List[ServiceData] = field(
        default_factory=list,
        metadata=dict(
            name="ServiceData",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    service_info: ServiceInfo = field(
        default=None,
        metadata=dict(
            name="ServiceInfo",
            type="Element",
            help=None,
        )
    )
    remark: List[Remark] = field(
        default_factory=list,
        metadata=dict(
            name="Remark",
            type="Element",
            help="Information regarding any specific for this service.",
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    emd: Emd = field(
        default=None,
        metadata=dict(
            name="EMD",
            type="Element",
            help=None,
        )
    )
    bundled_services: BundledServices = field(
        default=None,
        metadata=dict(
            name="BundledServices",
            type="Element",
            help=None,
        )
    )
    additional_info: List[AdditionalInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AdditionalInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=16
        )
    )
    fee_application: FeeApplication = field(
        default=None,
        metadata=dict(
            name="FeeApplication",
            type="Element",
            help="Specifies how the Optional Service fee is to be applied. The choices are Per One Way, Per Round Trip, Per Item (Per Piece), Per Travel, Per Ticket, Per 1 Kilo, Per 5 Kilos. Provider: 1G, 1V, 1P, 1J",
        )
    )
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=4
        )
    )
    price_range: List[PriceRange] = field(
        default_factory=list,
        metadata=dict(
            name="PriceRange",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=5
        )
    )
    tour_code: TourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element",
            help=None,
        )
    )
    branding_info: BrandingInfo = field(
        default=None,
        metadata=dict(
            name="BrandingInfo",
            type="Element",
            help=None,
        )
    )
    title: List[Title] = field(
        default_factory=list,
        metadata=dict(
            name="Title",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    optional_services_rule_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="OptionalServicesRuleRef",
            type="Attribute",
            help="UniqueID to associate a rule to the Optional Service",
        )
    )
    type: TypeMerchandisingService = field(
        default=None,
        metadata=dict(
            name="Type",
            type="Attribute",
            help="Specify the type of service offered (e.g. seats, baggage, etc.)",
            required=True
        )
    )
    confirmation: str = field(
        default=None,
        metadata=dict(
            name="Confirmation",
            type="Attribute",
            help="Confirmation number provided by the supplier",
        )
    )
    secondary_type: str = field(
        default=None,
        metadata=dict(
            name="SecondaryType",
            type="Attribute",
            help="The secondary option code type required for certain options",
        )
    )
    purchase_window: TypePurchaseWindow = field(
        default=None,
        metadata=dict(
            name="PurchaseWindow",
            type="Attribute",
            help="Describes when the Service is available for confirmation or purchase (e.g. Booking Only, Check-in Only, Anytime, etc.)",
        )
    )
    priority: int = field(
        default=None,
        metadata=dict(
            name="Priority",
            type="Attribute",
            help="Numeric value that represents the priority order of the Service",
        )
    )
    available: bool = field(
        default=None,
        metadata=dict(
            name="Available",
            type="Attribute",
            help="Boolean to describe whether the Service is available for sale or not",
        )
    )
    entitled: bool = field(
        default=None,
        metadata=dict(
            name="Entitled",
            type="Attribute",
            help="Boolean to describe whether the passenger is entitled for the service without charge or not",
        )
    )
    per_traveler: bool = field(
        default="true",
        metadata=dict(
            name="PerTraveler",
            type="Attribute",
            help="Boolean to describe whether the Amount on the Service is charged per traveler.",
        )
    )
    create_date: str = field(
        default=None,
        metadata=dict(
            name="CreateDate",
            type="Attribute",
            help="Timestamp when this service/offer got created.",
        )
    )
    payment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="PaymentRef",
            type="Attribute",
            help="Reference to a payment for merchandising services.",
        )
    )
    service_status: str = field(
        default=None,
        metadata=dict(
            name="ServiceStatus",
            type="Attribute",
            help="Specify the service status (e.g. active, canceled, etc.)",
        )
    )
    quantity: int = field(
        default=None,
        metadata=dict(
            name="Quantity",
            type="Attribute",
            help="The number of units availed for each optional service (e.g. 2 baggage availed will be specified as 2 in quantity for optional service BAGGAGE)",
        )
    )
    sequence_number: int = field(
        default=None,
        metadata=dict(
            name="SequenceNumber",
            type="Attribute",
            help="The sequence number associated with the OptionalService",
        )
    )
    service_sub_code: str = field(
        default=None,
        metadata=dict(
            name="ServiceSubCode",
            type="Attribute",
            help="The service subcode associated with the OptionalService",
            max_length=3.0
        )
    )
    ssrcode: TypeSsrcode = field(
        default=None,
        metadata=dict(
            name="SSRCode",
            type="Attribute",
            help="The SSR Code associated with the OptionalService",
        )
    )
    issuance_reason: str = field(
        default=None,
        metadata=dict(
            name="IssuanceReason",
            type="Attribute",
            help="A one-letter code specifying the reason for issuance of the OptionalService",
            min_length=1.0,
            max_length=1.0
        )
    )
    provider_defined_type: str = field(
        default=None,
        metadata=dict(
            name="ProviderDefinedType",
            type="Attribute",
            help="Original Type as sent by the provider",
            min_length=1.0,
            max_length=16.0
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    assess_indicator: TypeAssessIndicator = field(
        default=None,
        metadata=dict(
            name="AssessIndicator",
            type="Attribute",
            help="Indicates whether price is assessed by mileage or currency or both",
        )
    )
    mileage: int = field(
        default=None,
        metadata=dict(
            name="Mileage",
            type="Attribute",
            help="Indicates mileage fee/amount",
        )
    )
    applicable_fflevel: int = field(
        default=None,
        metadata=dict(
            name="ApplicableFFLevel",
            type="Attribute",
            help="Numerical value of the loyalty card level for which this service is available.",
            min_inclusive=0.0,
            max_inclusive=9.0
        )
    )
    private: bool = field(
        default=None,
        metadata=dict(
            name="Private",
            type="Attribute",
            help="Describes if service is private or not.",
        )
    )
    ssrfree_text: TypeSsrfreeText = field(
        default=None,
        metadata=dict(
            name="SSRFreeText",
            type="Attribute",
            help="Certain SSR types sent in OptionalService SSRCode require a free text message. For example, PETC Pet in Cabin.",
        )
    )
    is_pricing_approximate: bool = field(
        default=None,
        metadata=dict(
            name="IsPricingApproximate",
            type="Attribute",
            help="When set to True indicates that the pricing returned is approximate. Supported providers are MCH/ACH",
        )
    )
    chargeable: str = field(
        default=None,
        metadata=dict(
            name="Chargeable",
            type="Attribute",
            help="Indicates if the optional service is not offered, is available for a charge, or is included in the brand",
        )
    )
    inclusive_of_tax: bool = field(
        default=None,
        metadata=dict(
            name="InclusiveOfTax",
            type="Attribute",
            help="Identifies if the service was filed with a fee that is inclusive of tax.",
        )
    )
    interline_settlement_allowed: bool = field(
        default=None,
        metadata=dict(
            name="InterlineSettlementAllowed",
            type="Attribute",
            help="Identifies if the interline settlement is allowed in service .",
        )
    )
    geography_specification: str = field(
        default=None,
        metadata=dict(
            name="GeographySpecification",
            type="Attribute",
            help="Sector, Portion, Journey.",
        )
    )
    excess_weight_rate: str = field(
        default=None,
        metadata=dict(
            name="ExcessWeightRate",
            type="Attribute",
            help="The cost of the bag per unit weight.",
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            help="The Source of the optional service. The source can be ACH, MCE, or MCH.",
        )
    )
    viewable_only: bool = field(
        default=None,
        metadata=dict(
            name="ViewableOnly",
            type="Attribute",
            help="Describes if the OptionalService is viewable only or not. If viewable only then the service cannot be sold.",
        )
    )
    display_text: str = field(
        default=None,
        metadata=dict(
            name="DisplayText",
            type="Attribute",
            help="Title of the Optional Service. Provider: ACH",
        )
    )
    weight_in_excess: str = field(
        default=None,
        metadata=dict(
            name="WeightInExcess",
            type="Attribute",
            help="The excess weight of a bag. Providers: 1G, 1V, 1P, 1J",
        )
    )
    total_weight: str = field(
        default=None,
        metadata=dict(
            name="TotalWeight",
            type="Attribute",
            help="The total weight of a bag. Providers: 1G, 1V, 1P, 1J",
        )
    )
    baggage_unit_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BaggageUnitPrice",
            type="Attribute",
            help="The per unit price of baggage. Providers: 1G, 1V, 1P, 1J",
        )
    )
    first_piece: int = field(
        default=None,
        metadata=dict(
            name="FirstPiece",
            type="Attribute",
            help="Indicates the minimum occurrence of excess baggage.Provider: 1G, 1V, 1P, 1J.",
        )
    )
    last_piece: int = field(
        default=None,
        metadata=dict(
            name="LastPiece",
            type="Attribute",
            help="Indicates the maximum occurrence of excess baggage. Provider: 1G, 1V, 1P, 1J.",
        )
    )
    restricted: bool = field(
        default="false",
        metadata=dict(
            name="Restricted",
            type="Attribute",
            help="When set to “true”, the Optional Service is restricted by an embargo. Provider: 1G, 1V, 1P, 1J",
        )
    )
    is_reprice_required: bool = field(
        default="false",
        metadata=dict(
            name="IsRepriceRequired",
            type="Attribute",
            help="When set to “true”, the Optional Service must be re-priced. Provider: 1G, 1V, 1P, 1J",
        )
    )
    booked_quantity: str = field(
        default=None,
        metadata=dict(
            name="BookedQuantity",
            type="Attribute",
            help="Indicates the Optional Service quantity already booked. Provider: 1G, 1V, 1P, 1J",
        )
    )
    group: str = field(
        default=None,
        metadata=dict(
            name="Group",
            type="Attribute",
            help="Associates Optional Services with the same ServiceSub Code, Air Segment, Passenger, and EMD Associated Item. Provider:1G, 1V, 1P, 1J",
        )
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="The PCC or SID that booked the Optional Service.",
        )
    )
    tag: str = field(
        default=None,
        metadata=dict(
            name="Tag",
            type="Attribute",
            help="Optional service group name.",
            min_length=1.0,
            max_length=256.0
        )
    )
    display_order: int = field(
        default=None,
        metadata=dict(
            name="DisplayOrder",
            type="Attribute",
            help="Optional service group display order.",
            min_inclusive=0.0,
            max_inclusive=999.0
        )
    )


@dataclass
class RouteList:
    """
    Identifies the routes and sub-routes that were requested
    """

    route: List[Route] = field(
        default_factory=list,
        metadata=dict(
            name="Route",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class Row:
    """
    Identifies the row of in a seat map
    """

    facility: List[Facility] = field(
        default_factory=list,
        metadata=dict(
            name="Facility",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    characteristic: List[Characteristic] = field(
        default_factory=list,
        metadata=dict(
            name="Characteristic",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    number: int = field(
        default=None,
        metadata=dict(
            name="Number",
            type="Attribute",
            help=None,
            required=True
        )
    )
    search_traveler_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SearchTravelerRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class SearchAirLeg:
    """
    Search version of AirLeg used to specify search criteria
    """

    search_origin: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchOrigin",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    search_destination: List[TypeSearchLocation] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDestination",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_leg_modifiers: AirLegModifiers = field(
        default=None,
        metadata=dict(
            name="AirLegModifiers",
            type="Element",
            help=None,
        )
    )
    search_dep_time: List[TypeFlexibleTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchDepTime",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    search_arv_time: List[TypeTimeSpec] = field(
        default_factory=list,
        metadata=dict(
            name="SearchArvTime",
            type="Element",
            help="Specifies the preferred time within the time range. For 1G, 1V, 1P, 1J, it is supported for AvailabilitySearchReq (TimeRange must also be specified) and not supported for LowFareSearchReq. ACH does not support search by arrival time.",
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class SegmentModifiers:
    """
    To be used to modify the ticket modifiers for air segment
    """

    air_segment_ref: AirSegmentRef = field(
        default=None,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help=None,
            required=True
        )
    )
    ticket_validity: TicketValidity = field(
        default=None,
        metadata=dict(
            name="TicketValidity",
            type="Element",
            help="To be used to pass the ticket validity dates",
        )
    )
    baggage_allowance: BaggageAllowance = field(
        default=None,
        metadata=dict(
            name="BaggageAllowance",
            type="Element",
            help=None,
        )
    )
    ticket_designator: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="TicketDesignator",
            type="Element",
            help=None,
        )
    )


@dataclass
class StructuredFareRulesType:
    fare_rule_category_type: List[FareRuleCategoryTypes] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleCategoryType",
            type="Element",
            help="For FareRulesType element",
            min_occurs=0,
            max_occurs=99
        )
    )


@dataclass
class Ticket(AttrElementKeyResults):
    """
    The ticket that resulted from an air booking
    """

    coupon: List[Coupon] = field(
        default_factory=list,
        metadata=dict(
            name="Coupon",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=4
        )
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=6
        )
    )
    tour_code: List[TourCode] = field(
        default_factory=list,
        metadata=dict(
            name="TourCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    exchanged_ticket_info: List[ExchangedTicketInfo] = field(
        default_factory=list,
        metadata=dict(
            name="ExchangedTicketInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    ticket_number: TypeTicketNumber = field(
        default=None,
        metadata=dict(
            name="TicketNumber",
            type="Attribute",
            help=None,
            required=True
        )
    )
    ticket_status: TypeTicketStatus = field(
        default=None,
        metadata=dict(
            name="TicketStatus",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class TypeBaseAirSegment(Segment):
    sponsored_flt_info: SponsoredFltInfo = field(
        default=None,
        metadata=dict(
            name="SponsoredFltInfo",
            type="Element",
            help=None,
        )
    )
    codeshare_info: CodeshareInfo = field(
        default=None,
        metadata=dict(
            name="CodeshareInfo",
            type="Element",
            help=None,
        )
    )
    air_avail_info: List[AirAvailInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirAvailInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_details: List[FlightDetails] = field(
        default_factory=list,
        metadata=dict(
            name="FlightDetails",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_details_ref: List[FlightDetailsRef] = field(
        default_factory=list,
        metadata=dict(
            name="FlightDetailsRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    alternate_location_distance_ref: List[AlternateLocationDistanceRef] = field(
        default_factory=list,
        metadata=dict(
            name="AlternateLocationDistanceRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: Connection = field(
        default=None,
        metadata=dict(
            name="Connection",
            type="Element",
            help=None,
        )
    )
    sell_message: List[SellMessage] = field(
        default_factory=list,
        metadata=dict(
            name="SellMessage",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rail_coach_details: List[RailCoachDetails] = field(
        default_factory=list,
        metadata=dict(
            name="RailCoachDetails",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    open_segment: bool = field(
        default=None,
        metadata=dict(
            name="OpenSegment",
            type="Attribute",
            help="Indicates OpenSegment when True",
        )
    )
    group: int = field(
        default=None,
        metadata=dict(
            name="Group",
            type="Attribute",
            help="The Origin Destination Grouping of this segment.",
            required=True
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help="The carrier that is marketing this segment",
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.",
        )
    )
    flight_number: TypeFlightNumber = field(
        default=None,
        metadata=dict(
            name="FlightNumber",
            type="Attribute",
            help="The flight number under which the marketing carrier is marketing this flight",
        )
    )
    class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            help=None,
        )
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute",
            help="Identifies if this particular segment is E-Ticketable",
        )
    )
    equipment: TypeEquipment = field(
        default=None,
        metadata=dict(
            name="Equipment",
            type="Attribute",
            help="Identifies the equipment that this segment is operating under.",
        )
    )
    marriage_group: int = field(
        default=None,
        metadata=dict(
            name="MarriageGroup",
            type="Attribute",
            help="Identifies this segment as being a married segment. It is paired with other segments of the same value.",
        )
    )
    number_of_stops: int = field(
        default=None,
        metadata=dict(
            name="NumberOfStops",
            type="Attribute",
            help="Identifies the number of stops for each within the segment.",
        )
    )
    seamless: bool = field(
        default=None,
        metadata=dict(
            name="Seamless",
            type="Attribute",
            help="Identifies that this segment was sold via a direct access channel to the marketing carrier.",
        )
    )
    change_of_plane: bool = field(
        default="false",
        metadata=dict(
            name="ChangeOfPlane",
            type="Attribute",
            help="Indicates the traveler must change planes between flights.",
        )
    )
    guaranteed_payment_carrier: str = field(
        default=None,
        metadata=dict(
            name="GuaranteedPaymentCarrier",
            type="Attribute",
            help="Identifies that this segment has Guaranteed Payment Carrier.",
        )
    )
    host_token_ref: str = field(
        default=None,
        metadata=dict(
            name="HostTokenRef",
            type="Attribute",
            help="Identifies that this segment has Guaranteed Payment Carrier.",
        )
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    passive_provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="PassiveProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    optional_services_indicator: bool = field(
        default=None,
        metadata=dict(
            name="OptionalServicesIndicator",
            type="Attribute",
            help="Indicates true if flight provides optional services.",
        )
    )
    availability_source: TypeAvailabilitySource = field(
        default=None,
        metadata=dict(
            name="AvailabilitySource",
            type="Attribute",
            help="Indicates Availability source of AirSegment.",
        )
    )
    apisrequirements_ref: str = field(
        default=None,
        metadata=dict(
            name="APISRequirementsRef",
            type="Attribute",
            help="Reference to the APIS Requirements for this AirSegment.",
        )
    )
    black_listed: bool = field(
        default=None,
        metadata=dict(
            name="BlackListed",
            type="Attribute",
            help="Indicates blacklisted carriers which are banned from servicing points to, from and within the European Community.",
        )
    )
    operational_status: str = field(
        default=None,
        metadata=dict(
            name="OperationalStatus",
            type="Attribute",
            help="Refers to the flight operational status for the segment. This attribute will only be returned in the AvailabilitySearchRsp and not used/returned in any other request/responses. If this attribute is not returned back in the response, it means the flight is operational and not past scheduled departure.",
        )
    )
    number_in_party: int = field(
        default=None,
        metadata=dict(
            name="NumberInParty",
            type="Attribute",
            help="Number of person traveling in this air segment excluding the number of infants on lap.",
            min_inclusive=1.0,
            max_inclusive=99.0
        )
    )
    rail_coach_number: str = field(
        default=None,
        metadata=dict(
            name="RailCoachNumber",
            type="Attribute",
            help="Coach number for which rail seatmap/coachmap is returned.",
            max_length=4.0
        )
    )
    booking_date: str = field(
        default=None,
        metadata=dict(
            name="BookingDate",
            type="Attribute",
            help="Used for rapid reprice. The date the booking was made. Providers: 1G/1V/1P/1S/1A",
        )
    )
    flown_segment: bool = field(
        default="false",
        metadata=dict(
            name="FlownSegment",
            type="Attribute",
            help="Used for rapid reprice. Tells whether or not the air segment has been flown. Providers: 1G/1V/1P/1S/1A",
        )
    )
    schedule_change: bool = field(
        default="false",
        metadata=dict(
            name="ScheduleChange",
            type="Attribute",
            help="Used for rapid reprice. Tells whether or not the air segment had a schedule change by the carrier. This tells rapid reprice that the change in the air segment was involuntary and because of a schedule change, not because the user is changing the segment. Providers: 1G/1V/1P/1S/1A",
        )
    )
    brand_indicator: str = field(
        default=None,
        metadata=dict(
            name="BrandIndicator",
            type="Attribute",
            help="Value “B” specifies that the carrier supports Rich Content and Branding. The Brand Indicator is only returned in the availability search response. Provider: 1G, 1V, 1P, 1J, ACH",
        )
    )


@dataclass
class AirSegment(TypeBaseAirSegment):
    """
    An Air marketable travel segment.
    """

    pass


@dataclass
class BaggageAllowanceInfo(BaseBaggageAllowanceInfo):
    """
    Information related to Baggage allowance like URL,Height,Weight etc.
    """

    bag_details: List[BagDetails] = field(
        default_factory=list,
        metadata=dict(
            name="BagDetails",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    traveler_type: TypePtc = field(
        default=None,
        metadata=dict(
            name="TravelerType",
            type="Attribute",
            help=None,
        )
    )
    fare_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FareDisplay:
    """
    Fare/Tariff Display
    """

    fare_display_rule: FareDisplayRule = field(
        default=None,
        metadata=dict(
            name="FareDisplayRule",
            type="Element",
            help=None,
            required=True
        )
    )
    fare_pricing: List[FarePricing] = field(
        default_factory=list,
        metadata=dict(
            name="FarePricing",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    fare_restriction: List[FareRestriction] = field(
        default_factory=list,
        metadata=dict(
            name="FareRestriction",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    fare_routing_information: FareRoutingInformation = field(
        default=None,
        metadata=dict(
            name="FareRoutingInformation",
            type="Element",
            help=None,
        )
    )
    fare_mileage_information: FareMileageInformation = field(
        default=None,
        metadata=dict(
            name="FareMileageInformation",
            type="Element",
            help=None,
        )
    )
    air_fare_display_rule_key: AirFareDisplayRuleKey = field(
        default=None,
        metadata=dict(
            name="AirFareDisplayRuleKey",
            type="Element",
            help=None,
        )
    )
    booking_code: List[BookingCode] = field(
        default_factory=list,
        metadata=dict(
            name="BookingCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    addl_booking_code_information: AddlBookingCodeInformation = field(
        default=None,
        metadata=dict(
            name="AddlBookingCodeInformation",
            type="Element",
            help=None,
        )
    )
    fare_rule_failure_info: FareRuleFailureInfo = field(
        default=None,
        metadata=dict(
            name="FareRuleFailureInfo",
            type="Element",
            help="Returns fare rule failure info for Non Valid fares.",
        )
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata=dict(
            name="PriceChange",
            type="Element",
            help="Indicates a price change is found in Fare Control Manager",
            min_occurs=0,
            max_occurs=99
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
            required=True
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help=None,
            required=True
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
            required=True
        )
    )
    trip_type: TypeFareTripType = field(
        default=None,
        metadata=dict(
            name="TripType",
            type="Attribute",
            help=None,
        )
    )
    fare_type_code: TypeFareTypeCode = field(
        default=None,
        metadata=dict(
            name="FareTypeCode",
            type="Attribute",
            help=None,
        )
    )
    special_fare: bool = field(
        default=None,
        metadata=dict(
            name="SpecialFare",
            type="Attribute",
            help=None,
        )
    )
    instant_purchase: bool = field(
        default=None,
        metadata=dict(
            name="InstantPurchase",
            type="Attribute",
            help=None,
        )
    )
    eligibility_restricted: bool = field(
        default=None,
        metadata=dict(
            name="EligibilityRestricted",
            type="Attribute",
            help=None,
        )
    )
    flight_restricted: bool = field(
        default=None,
        metadata=dict(
            name="FlightRestricted",
            type="Attribute",
            help=None,
        )
    )
    stopovers_restricted: bool = field(
        default=None,
        metadata=dict(
            name="StopoversRestricted",
            type="Attribute",
            help=None,
        )
    )
    transfers_restricted: bool = field(
        default=None,
        metadata=dict(
            name="TransfersRestricted",
            type="Attribute",
            help=None,
        )
    )
    blackouts_exist: bool = field(
        default=None,
        metadata=dict(
            name="BlackoutsExist",
            type="Attribute",
            help=None,
        )
    )
    accompanied_travel: bool = field(
        default=None,
        metadata=dict(
            name="AccompaniedTravel",
            type="Attribute",
            help=None,
        )
    )
    mile_or_route_based_fare: TypeMileOrRouteBasedFare = field(
        default=None,
        metadata=dict(
            name="MileOrRouteBasedFare",
            type="Attribute",
            help=None,
        )
    )
    global_indicator: TypeAtpcoglobalIndicator = field(
        default=None,
        metadata=dict(
            name="GlobalIndicator",
            type="Attribute",
            help=None,
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Returns the origin airport or city code for which this tariff is applicable.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Returns the destination airport or city code for which this tariff is applicable.",
        )
    )
    fare_ticketing_code: str = field(
        default=None,
        metadata=dict(
            name="FareTicketingCode",
            type="Attribute",
            help="Returns the ticketing code for which this tariff is applicable.",
        )
    )
    fare_ticketing_designator: TypeTicketDesignator = field(
        default=None,
        metadata=dict(
            name="FareTicketingDesignator",
            type="Attribute",
            help="Returns the ticketing designator for which this tariff is applicable.",
        )
    )


@dataclass
class FareRule(AttrProviderSupplier):
    """
    Fare Rule Container
    """

    fare_rule_long: List[FareRuleLong] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleLong",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_rule_short: List[FareRuleShort] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleShort",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    rule_advanced_purchase: RuleAdvancedPurchase = field(
        default=None,
        metadata=dict(
            name="RuleAdvancedPurchase",
            type="Element",
            help=None,
        )
    )
    rule_length_of_stay: RuleLengthOfStay = field(
        default=None,
        metadata=dict(
            name="RuleLengthOfStay",
            type="Element",
            help=None,
        )
    )
    rule_charges: RuleCharges = field(
        default=None,
        metadata=dict(
            name="RuleCharges",
            type="Element",
            help=None,
        )
    )
    fare_rule_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="FareRuleResultMessage",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    structured_fare_rules: StructuredFareRulesType = field(
        default=None,
        metadata=dict(
            name="StructuredFareRules",
            type="Element",
            help=None,
        )
    )
    fare_info_ref: str = field(
        default=None,
        metadata=dict(
            name="FareInfoRef",
            type="Attribute",
            help=None,
        )
    )
    rule_number: str = field(
        default=None,
        metadata=dict(
            name="RuleNumber",
            type="Attribute",
            help=None,
        )
    )
    source: str = field(
        default=None,
        metadata=dict(
            name="Source",
            type="Attribute",
            help=None,
        )
    )
    tariff_number: str = field(
        default=None,
        metadata=dict(
            name="TariffNumber",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class FlightOptionsList:
    """
    List of Flight Options for the itinerary.
    """

    flight_option: List[FlightOption] = field(
        default_factory=list,
        metadata=dict(
            name="FlightOption",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class OptionalServices:
    """
    A wrapper for all the information regarding each of the Optional services
    """

    optional_services_total: "OptionalServices.OptionalServicesTotal" = field(
        default=None,
        metadata=dict(
            name="OptionalServicesTotal",
            type="Element",
            help="The total fares, fees and taxes associated with the Optional Services",
        )
    )
    optional_service: List[OptionalService] = field(
        default_factory=list,
        metadata=dict(
            name="OptionalService",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    grouped_option_info: List[GroupedOptionInfo] = field(
        default_factory=list,
        metadata=dict(
            name="GroupedOptionInfo",
            type="Element",
            help="Details about an unselected or 'other' option when optional services are grouped together.",
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_service_rules: List[ServiceRuleType] = field(
        default_factory=list,
        metadata=dict(
            name="OptionalServiceRules",
            type="Element",
            help="Holds the rules for selecting the optional service in the itinerary",
            min_occurs=0,
            max_occurs=999
        )
    )

    @dataclass
    class OptionalServicesTotal(AttrPrices):
        tax_info: List[TaxInfo] = field(
            default_factory=list,
            metadata=dict(
                name="TaxInfo",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=999
            )
        )
        fee_info: List[FeeInfo] = field(
            default_factory=list,
            metadata=dict(
                name="FeeInfo",
                type="Element",
                help=None,
                min_occurs=0,
                max_occurs=999
            )
        )


@dataclass
class PrePayProfileInfo:
    """
    PrePay Profile associated with the customer
    """

    pre_pay_id: PrePayId = field(
        default=None,
        metadata=dict(
            name="PrePayId",
            type="Element",
            help="Pre pay unique identifier detail.This information block is returned both in list and detail retrieve transactions.Example flight pass number",
            required=True
        )
    )
    pre_pay_customer: PrePayCustomer = field(
        default=None,
        metadata=dict(
            name="PrePayCustomer",
            type="Element",
            help="Pre pay customer detail.This information block is returned both in list and detail retrieve transactions.",
        )
    )
    pre_pay_account: PrePayAccount = field(
        default=None,
        metadata=dict(
            name="PrePayAccount",
            type="Element",
            help="Pre pay account detail.This information block is returned both in list and detail retrieve transactions.",
        )
    )
    affiliations: Affiliations = field(
        default=None,
        metadata=dict(
            name="Affiliations",
            type="Element",
            help="Pre pay affiliations detail.This information block is returned only in detail retrieve transactions.",
        )
    )
    account_related_rules: AccountRelatedRules = field(
        default=None,
        metadata=dict(
            name="AccountRelatedRules",
            type="Element",
            help="Pre pay account related rules.This information block is returned only in detail retrieve transactions.",
        )
    )
    status_code: str = field(
        default=None,
        metadata=dict(
            name="StatusCode",
            type="Attribute",
            help="Customer pre pay profile status code(One of Marked for deletion,Lapsed,Terminated,Active,Inactive)",
        )
    )
    creator_id: TypeCardNumber = field(
        default=None,
        metadata=dict(
            name="CreatorID",
            type="Attribute",
            help="This is the loyalty card number of the person who originally purchased/setup the flight pass",
        )
    )


@dataclass
class Rows:
    """
    A wrapper for all the information regarding each of the rows. Providers: ACH, 1G, 1V, 1P, 1J
    """

    row: List[Row] = field(
        default_factory=list,
        metadata=dict(
            name="Row",
            type="Element",
            help="Provider: 1G,1V,1P,1J,ACH,MCH.",
            min_occurs=0,
            max_occurs=999
        )
    )
    segment_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="SegmentRef",
            type="Attribute",
            help="Specifies the AirSegment the seat map is for. Providers: ACH, 1G, 1V, 1P, 1J",
        )
    )


@dataclass
class TicketingModifiers(AttrElementKeyResults):
    """
    A container to identify individual ticketing modifiers.
    """

    booking_traveler_ref: List[TypeRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help="Reference to a booking traveler for which ticketing modifier is applied.",
            min_occurs=0,
            max_occurs=999
        )
    )
    net_remit: TypeTicketModifierAmountType = field(
        default=None,
        metadata=dict(
            name="NetRemit",
            type="Element",
            help="Allows an agency to override the net remittance amount - varies by BSP agreement",
        )
    )
    net_fare: TypeTicketModifierAmountType = field(
        default=None,
        metadata=dict(
            name="NetFare",
            type="Element",
            help="Net Fare amount for a ticketed fare",
        )
    )
    actual_selling_fare: TypeTicketModifierAmountType = field(
        default=None,
        metadata=dict(
            name="ActualSellingFare",
            type="Element",
            help="Allows an agency to report an Actual Selling Fare as part of the net remittance BSP agreement",
        )
    )
    invoice_fare: TypeTicketModifierAccountingType = field(
        default=None,
        metadata=dict(
            name="InvoiceFare",
            type="Element",
            help="Allows an agency to report an Invoice Fare as part of the net remittance BSP agreement",
        )
    )
    corporate_discount: TypeTicketModifierAccountingType = field(
        default=None,
        metadata=dict(
            name="CorporateDiscount",
            type="Element",
            help="Allows an agency to add a corporate discount to the itinerary to be ticketed",
        )
    )
    accounting_info: TypeTicketModifierAccountingType = field(
        default=None,
        metadata=dict(
            name="AccountingInfo",
            type="Element",
            help="Allows an agency to report Accounting Information as part of the net remittance BSP agreement",
        )
    )
    bulk_ticket: "TicketingModifiers.BulkTicket" = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Element",
            help="Allows an agency to update the fare as a Bulk ticket - Optional SuppressOnFareCalc attribute will control how fare calculation is printed on the ticket",
        )
    )
    group_tour: TypeBulkTicketModifierType = field(
        default=None,
        metadata=dict(
            name="GroupTour",
            type="Element",
            help="Allows an agency to update the fare as a Group Tour (inclusive tour) ticket - Optional SuppressOnFareCalc attribute will control how fare calculation is printed on the ticket",
        )
    )
    commission: Commission = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            help="Allows an agency to update the commission to a new or different commission rate which will be applied at time of ticketing. The commission Modifier allows the user specify how the commission change is to applied",
        )
    )
    tour_code: TourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Element",
            help="Allows an agency to modify the tour code information on the ticket",
        )
    )
    ticket_endorsement: List[TicketEndorsement] = field(
        default_factory=list,
        metadata=dict(
            name="TicketEndorsement",
            type="Element",
            help="Allows an agency to add user defined ticketing endorsements the ticket",
            min_occurs=0,
            max_occurs=3
        )
    )
    value_modifier: TypeTicketModifierValueType = field(
        default=None,
        metadata=dict(
            name="ValueModifier",
            type="Element",
            help="Allows an agency to modify value or commission of the ticket. The modifier is generic and depends on the specific GDS and BSP implementation",
        )
    )
    document_select: DocumentSelect = field(
        default=None,
        metadata=dict(
            name="DocumentSelect",
            type="Element",
            help=None,
        )
    )
    document_options: DocumentOptions = field(
        default=None,
        metadata=dict(
            name="DocumentOptions",
            type="Element",
            help=None,
        )
    )
    segment_select: SegmentSelect = field(
        default=None,
        metadata=dict(
            name="SegmentSelect",
            type="Element",
            help=None,
        )
    )
    segment_modifiers: List[SegmentModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="SegmentModifiers",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_locator: SupplierLocator = field(
        default=None,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            help=None,
        )
    )
    destination_purpose_code: DestinationPurposeCode = field(
        default=None,
        metadata=dict(
            name="DestinationPurposeCode",
            type="Element",
            help=None,
        )
    )
    language_option: List[LanguageOption] = field(
        default_factory=list,
        metadata=dict(
            name="LanguageOption",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=2
        )
    )
    land_charges: LandCharges = field(
        default=None,
        metadata=dict(
            name="LandCharges",
            type="Element",
            help=None,
        )
    )
    print_blank_form_itinerary: PrintBlankFormItinerary = field(
        default=None,
        metadata=dict(
            name="PrintBlankFormItinerary",
            type="Element",
            help=None,
        )
    )
    exclude_ticketing: ExcludeTicketing = field(
        default=None,
        metadata=dict(
            name="ExcludeTicketing",
            type="Element",
            help=None,
        )
    )
    exempt_obfee: ExemptObfee = field(
        default=None,
        metadata=dict(
            name="ExemptOBFee",
            type="Element",
            help=None,
        )
    )
    is_primary_di: bool = field(
        default="false",
        metadata=dict(
            name="IsPrimaryDI",
            type="Attribute",
            help="Indicates if the DI is Primary DI. 1P only",
        )
    )
    document_instruction_number: str = field(
        default=None,
        metadata=dict(
            name="DocumentInstructionNumber",
            type="Attribute",
            help="The Document Instruction line number. 1P only",
        )
    )
    reference: StringLength1to30 = field(
        default=None,
        metadata=dict(
            name="Reference",
            type="Attribute",
            help="Identifies if TicketingModifiers contains DI line information. 1P only.",
        )
    )
    status: str = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="DI line status - ex:Ticketed",
            max_length=30.0
        )
    )
    free_text: str = field(
        default=None,
        metadata=dict(
            name="FreeText",
            type="Attribute",
            help="DI line information shown as free text as in Host. 1P only",
            max_length=756.0
        )
    )
    name_number: str = field(
        default=None,
        metadata=dict(
            name="NameNumber",
            type="Attribute",
            help="Host Name Number",
        )
    )
    ticket_record: str = field(
        default=None,
        metadata=dict(
            name="TicketRecord",
            type="Attribute",
            help="Ticket Record Number",
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="Allows an agency to specify the Plating Carrier for ticketing",
        )
    )
    exempt_vat: bool = field(
        default=None,
        metadata=dict(
            name="ExemptVAT",
            type="Attribute",
            help="Allows an agency to update if VAT is Exemtped on the fare.",
        )
    )
    net_remit_applied: bool = field(
        default=None,
        metadata=dict(
            name="NetRemitApplied",
            type="Attribute",
            help="Indicator to the BSP net remittance scheme applies to ticketed fare.",
        )
    )
    free_ticket: bool = field(
        default=None,
        metadata=dict(
            name="FreeTicket",
            type="Attribute",
            help="Indicates free ticket.",
        )
    )
    currency_override_code: str = field(
        default=None,
        metadata=dict(
            name="CurrencyOverrideCode",
            type="Attribute",
            help="This modifier allows an agency to specify the currency like L for Local, E for Euro, U for USD, C for CAD (Canadian dollars).",
            length=1
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )

    @dataclass
    class BulkTicket(TypeBulkTicketModifierType):
        non_refundable: bool = field(
            default=None,
            metadata=dict(
                name="NonRefundable",
                type="Attribute",
                help="Indicates bulk ticket being non-refundable",
            )
        )


@dataclass
class AirItinerary:
    """
    A container for an Air only travel itinerary.
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    apisrequirements: List[Apisrequirements] = field(
        default_factory=list,
        metadata=dict(
            name="APISRequirements",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPricingTicketingModifiers:
    """
    AirPricing TicketingModifier information - used to associate Ticketing Modifiers with one or more AirPricingInfos/ProviderReservationInfo
    """

    air_pricing_info_ref: List[AirPricingInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers: TicketingModifiers = field(
        default=None,
        metadata=dict(
            name="TicketingModifiers",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class AirSegmentError:
    """
    Container to return error messages corresponding to AirSegment
    """

    air_segment: AirSegment = field(
        default=None,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            required=True
        )
    )
    error_message: str = field(
        default=None,
        metadata=dict(
            name="ErrorMessage",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class AirSegmentList:
    """
    The shared object list of AirSegments
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirSolution:
    """
    Defines an air solution that is comprised of an itinerary (the segments) along with the passengers.
    """

    search_traveler: List[SearchTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="SearchTraveler",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=9
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=16
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=16
        )
    )
    fare_basis: List[FareBasis] = field(
        default_factory=list,
        metadata=dict(
            name="FareBasis",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=16
        )
    )


@dataclass
class BaggageAllowances:
    """
    Details of Baggage allowance
    """

    baggage_allowance_info: List[BaggageAllowanceInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageAllowanceInfo",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    carry_on_allowance_info: List[CarryOnAllowanceInfo] = field(
        default_factory=list,
        metadata=dict(
            name="CarryOnAllowanceInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    embargo_info: List[EmbargoInfo] = field(
        default_factory=list,
        metadata=dict(
            name="EmbargoInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class Brand:
    """
    Commercially recognized product offered by an airline
    """

    title: List[Title] = field(
        default_factory=list,
        metadata=dict(
            name="Title",
            type="Element",
            help="The additional titles associated to the brand",
            min_occurs=0,
            max_occurs=2
        )
    )
    text: List[Text] = field(
        default_factory=list,
        metadata=dict(
            name="Text",
            type="Element",
            help="Text associated to the brand",
            min_occurs=0,
            max_occurs=5
        )
    )
    image_location: List[ImageLocation] = field(
        default_factory=list,
        metadata=dict(
            name="ImageLocation",
            type="Element",
            help="Images associated to the brand",
            min_occurs=0,
            max_occurs=3
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help=None,
        )
    )
    rules: List[Rules] = field(
        default_factory=list,
        metadata=dict(
            name="Rules",
            type="Element",
            help="Brand rules",
            min_occurs=0,
            max_occurs=99
        )
    )
    service_associations: ServiceAssociations = field(
        default=None,
        metadata=dict(
            name="ServiceAssociations",
            type="Element",
            help="Service associated with this brand",
        )
    )
    upsell_brand: UpsellBrand = field(
        default=None,
        metadata=dict(
            name="UpsellBrand",
            type="Element",
            help="The unique identifier of the Upsell brand",
        )
    )
    applicable_segment: List[TypeApplicableSegment] = field(
        default_factory=list,
        metadata=dict(
            name="ApplicableSegment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    default_brand_detail: List[DefaultBrandDetail] = field(
        default_factory=list,
        metadata=dict(
            name="DefaultBrandDetail",
            type="Element",
            help="Default brand details.",
            min_occurs=0,
            max_occurs=99
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help="Brand Key",
        )
    )
    brand_id: TypeBrandId = field(
        default=None,
        metadata=dict(
            name="BrandID",
            type="Attribute",
            help="The unique identifier of the brand",
        )
    )
    name: str = field(
        default=None,
        metadata=dict(
            name="Name",
            type="Attribute",
            help="The Title of the brand",
        )
    )
    air_itinerary_details_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="AirItineraryDetailsRef",
            type="Attribute",
            help="AirItinerary associated with this brand",
        )
    )
    up_sell_brand_id: TypeBrandId = field(
        default=None,
        metadata=dict(
            name="UpSellBrandID",
            type="Attribute",
            help=None,
        )
    )
    brand_found: bool = field(
        default=None,
        metadata=dict(
            name="BrandFound",
            type="Attribute",
            help="Indicates whether brand for the fare was found for carrier or not",
        )
    )
    up_sell_brand_found: bool = field(
        default=None,
        metadata=dict(
            name="UpSellBrandFound",
            type="Attribute",
            help="Indicates whether upsell brand for the fare was found for carrier or not",
        )
    )
    branded_details_available: bool = field(
        default=None,
        metadata=dict(
            name="BrandedDetailsAvailable",
            type="Attribute",
            help="Indicates if full details of the brand is available",
        )
    )
    carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="Carrier",
            type="Attribute",
            help=None,
        )
    )
    brand_tier: StringLength1to10 = field(
        default=None,
        metadata=dict(
            name="BrandTier",
            type="Attribute",
            help="Modifier to price by specific brand tier number.",
        )
    )
    brand_maintained: StringLength1to99 = field(
        default=None,
        metadata=dict(
            name="BrandMaintained",
            type="Attribute",
            help="Indicates whether the brand was maintained from the original ticket.",
        )
    )


@dataclass
class ExchangeAirSegment:
    """
    A container to define segment and cabin class in order to process an exchange
    """

    air_segment: AirSegment = field(
        default=None,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            required=True
        )
    )
    cabin_class: CabinClass = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Element",
            help=None,
            required=True
        )
    )
    fare_basis_code: str = field(
        default=None,
        metadata=dict(
            name="FareBasisCode",
            type="Attribute",
            help="The fare basis code to be used for exchange of this segment.",
        )
    )


@dataclass
class JourneyData:
    """
    Performs journey aware air availability
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=99
        )
    )


@dataclass
class TcrrefundBundle:
    """
    Used both in request and response
    """

    air_refund_info: AirRefundInfo = field(
        default=None,
        metadata=dict(
            name="AirRefundInfo",
            type="Element",
            help=None,
            required=True
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Itinerary level taxes",
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            help="The identifying number for a Ticketless Air Reservation.",
            required=True
        )
    )
    refund_type: str = field(
        default=None,
        metadata=dict(
            name="RefundType",
            type="Attribute",
            help="Specifies whether this bundle was auto or manually generated",
            required=True
        )
    )
    refund_access_code: RefundAccessCode = field(
        default=None,
        metadata=dict(
            name="RefundAccessCode",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirSegmentData:
    """
    The shared object list of AirsegmentData
    """

    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    baggage_allowance: List[BaggageAllowance] = field(
        default_factory=list,
        metadata=dict(
            name="BaggageAllowance",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    brand: List[Brand] = field(
        default_factory=list,
        metadata=dict(
            name="Brand",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    cabin_class: str = field(
        default=None,
        metadata=dict(
            name="CabinClass",
            type="Attribute",
            help="Specifies Cabin class for a group of class of services. Cabin class is not identified if it is not present.",
        )
    )
    class_of_service: TypeClassOfService = field(
        default=None,
        metadata=dict(
            name="ClassOfService",
            type="Attribute",
            help=None,
        )
    )


@dataclass
class AirSegmentSellFailureInfo:
    """
    Container to return air segment sell failures.
    """

    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentError",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AvailabilityErrorInfo(TypeErrorInfo):
    air_segment_error: List[AirSegmentError] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentError",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class FareInfo(AttrElementKeyResults):
    """
    Information about this fare component
    """

    fare_ticket_designator: List[FareTicketDesignator] = field(
        default_factory=list,
        metadata=dict(
            name="FareTicketDesignator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_surcharge: List[FareSurcharge] = field(
        default_factory=list,
        metadata=dict(
            name="FareSurcharge",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    account_code: List[AccountCode] = field(
        default_factory=list,
        metadata=dict(
            name="AccountCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    contract_code: List[ContractCode] = field(
        default_factory=list,
        metadata=dict(
            name="ContractCode",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    endorsement: List[Endorsement] = field(
        default_factory=list,
        metadata=dict(
            name="Endorsement",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    baggage_allowance: BaggageAllowance = field(
        default=None,
        metadata=dict(
            name="BaggageAllowance",
            type="Element",
            help=None,
        )
    )
    fare_rule_key: FareRuleKey = field(
        default=None,
        metadata=dict(
            name="FareRuleKey",
            type="Element",
            help=None,
        )
    )
    fare_rule_failure_info: FareRuleFailureInfo = field(
        default=None,
        metadata=dict(
            name="FareRuleFailureInfo",
            type="Element",
            help=None,
        )
    )
    fare_remark_ref: List[FareRemarkRef] = field(
        default_factory=list,
        metadata=dict(
            name="FareRemarkRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    brand: Brand = field(
        default=None,
        metadata=dict(
            name="Brand",
            type="Element",
            help=None,
        )
    )
    commission: Commission = field(
        default=None,
        metadata=dict(
            name="Commission",
            type="Element",
            help="Specifies the Commission for Agency for a particular Fare component. Apllicable Providers are 1G and 1V.",
        )
    )
    fare_attributes: str = field(
        default=None,
        metadata=dict(
            name="FareAttributes",
            type="Element",
            help="Returns all fare attributes separated by pipe ‘|’. Attribute information is returned by comma separated values for each attribute. These information include attribute number, chargeable indicator and supplementary info. Attribute numbers: 1 - Checked Bag, 2 - Carry On, 3 - Rebooking, 4 - Refund, 5 - Seats, 6 - Meals, 7 - WiFi. Chargeable Indicator: Y - Chargeable, N - Not Chargeable. Supplementary Information that will be returned is : For 1 and 2 - Baggage weights. For 3 – Changeable Info. For 4 – Refundable Info. For 5 - Seat description. For 6 – Meal description. For 7 – WiFi description. Example: 1,Y,23|1,N,50|2,N,8|3,N,CHANGEABLE|4,Y,REFUNDABLE|5,N,SEATING|5,N,MIDDLE|6,Y,SOFT DRINK|6,N,ALCOHOLIC DRINK|6,Y,SNACK|7,X,WIFI",
        )
    )
    change_penalty: TypeFarePenalty = field(
        default=None,
        metadata=dict(
            name="ChangePenalty",
            type="Element",
            help="The penalty (if any) to change the itinerary",
        )
    )
    cancel_penalty: TypeFarePenalty = field(
        default=None,
        metadata=dict(
            name="CancelPenalty",
            type="Element",
            help="The penalty (if any) to cancel the fare",
        )
    )
    fare_rules_filter: FareRulesFilter = field(
        default=None,
        metadata=dict(
            name="FareRulesFilter",
            type="Element",
            help=None,
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    fare_basis: str = field(
        default=None,
        metadata=dict(
            name="FareBasis",
            type="Attribute",
            help="The fare basis code for this fare",
            required=True
        )
    )
    passenger_type_code: TypePtc = field(
        default=None,
        metadata=dict(
            name="PassengerTypeCode",
            type="Attribute",
            help="The PTC that is associated with this fare.",
            required=True
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="Returns the airport or city code that defines the origin market for this fare.",
            required=True
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="Returns the airport or city code that defines the destination market for this fare.",
            required=True
        )
    )
    effective_date: str = field(
        default=None,
        metadata=dict(
            name="EffectiveDate",
            type="Attribute",
            help="Returns the date on which this fare was quoted",
            required=True
        )
    )
    travel_date: str = field(
        default=None,
        metadata=dict(
            name="TravelDate",
            type="Attribute",
            help="Returns the departure date of the first segment that uses this fare.",
        )
    )
    departure_date: str = field(
        default=None,
        metadata=dict(
            name="DepartureDate",
            type="Attribute",
            help="Returns the departure date of the first segment of the journey.",
        )
    )
    amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Amount",
            type="Attribute",
            help=None,
        )
    )
    private_fare: TypePrivateFare = field(
        default=None,
        metadata=dict(
            name="PrivateFare",
            type="Attribute",
            help=None,
        )
    )
    negotiated_fare: bool = field(
        default=None,
        metadata=dict(
            name="NegotiatedFare",
            type="Attribute",
            help="Identifies the fare as a Negotiated Fare.",
        )
    )
    tour_code: TypeTourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            help=None,
        )
    )
    waiver_code: str = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Attribute",
            help=None,
        )
    )
    not_valid_before: str = field(
        default=None,
        metadata=dict(
            name="NotValidBefore",
            type="Attribute",
            help="Fare not valid before this date.",
        )
    )
    not_valid_after: str = field(
        default=None,
        metadata=dict(
            name="NotValidAfter",
            type="Attribute",
            help="Fare not valid after this date.",
        )
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="Provider PseudoCityCode associated with private fare.",
        )
    )
    fare_family: TypeFareFamily = field(
        default=None,
        metadata=dict(
            name="FareFamily",
            type="Attribute",
            help="An alpha-numeric string which denotes fare family. Some carriers may return this in lieu of or in addition to the CabinClass.",
        )
    )
    promotional_fare: bool = field(
        default=None,
        metadata=dict(
            name="PromotionalFare",
            type="Attribute",
            help="Boolean to describe whether the Fare is Promotional fare or not.",
        )
    )
    car_code: TypeCarCode = field(
        default=None,
        metadata=dict(
            name="CarCode",
            type="Attribute",
            help=None,
        )
    )
    value_code: TypeValueCode = field(
        default=None,
        metadata=dict(
            name="ValueCode",
            type="Attribute",
            help=None,
        )
    )
    bulk_ticket: bool = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Whether the ticket can be issued as bulk for this fare. Providers supported: Worldspan and JAL",
        )
    )
    inclusive_tour: bool = field(
        default=None,
        metadata=dict(
            name="InclusiveTour",
            type="Attribute",
            help="Whether the ticket can be issued as part of included package for this fare. Providers supported: Worldspan and JAL",
        )
    )
    value: str = field(
        default=None,
        metadata=dict(
            name="Value",
            type="Attribute",
            help="Used in rapid reprice",
        )
    )
    supplier_code: TypeSupplierCode = field(
        default=None,
        metadata=dict(
            name="SupplierCode",
            type="Attribute",
            help="Code of the provider returning this fare info",
        )
    )
    tax_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TaxAmount",
            type="Attribute",
            help="Currency code and value for the approximate tax amount for this fare component.",
        )
    )


@dataclass
class AirExchangeMultiQuoteOption:
    """
    The shared object list of AirExchangeMultiQuoteOptions
    """

    air_segment_data: List[AirSegmentData] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentData",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element",
            help=None,
        )
    )
    air_exchange_bundle_list: List[AirExchangeBundleList] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundleList",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPricingInfo(AttrPrices, AttrProviderSupplier, AttrElementKeyResults, AttrPolicyMarking):
    """
    Per traveler type pricing breakdown. This will reflect the pricing for all travelers of the specified type.
    """

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_status: FareStatus = field(
        default=None,
        metadata=dict(
            name="FareStatus",
            type="Element",
            help=None,
        )
    )
    fare_info_ref: List[FareInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_info: List[BookingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="BookingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_calc: FareCalc = field(
        default=None,
        metadata=dict(
            name="FareCalc",
            type="Element",
            help=None,
        )
    )
    passenger_type: List[PassengerType] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerType",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )
    payment_ref: List[PaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="PaymentRef",
            type="Element",
            help="The reference to the Payment if Air Pricing is charged",
            min_occurs=0,
            max_occurs=999
        )
    )
    change_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata=dict(
            name="ChangePenalty",
            type="Element",
            help="The penalty (if any) to change the itinerary",
            min_occurs=0,
            max_occurs=999
        )
    )
    cancel_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata=dict(
            name="CancelPenalty",
            type="Element",
            help="The penalty (if any) to cancel the fare",
            min_occurs=0,
            max_occurs=999
        )
    )
    no_show_penalty: List[TypeFarePenalty] = field(
        default_factory=list,
        metadata=dict(
            name="NoShowPenalty",
            type="Element",
            help="The NoShow penalty (if any)",
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    adjustment: List[Adjustment] = field(
        default_factory=list,
        metadata=dict(
            name="Adjustment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    yield_value: List[Yield] = field(
        default_factory=list,
        metadata=dict(
            name="Yield",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_modifiers: AirPricingModifiers = field(
        default=None,
        metadata=dict(
            name="AirPricingModifiers",
            type="Element",
            help=None,
        )
    )
    ticketing_modifiers_ref: List[TicketingModifiersRef] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiersRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_pricing_modifiers: List[AirSegmentPricingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentPricingModifiers",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    flight_options_list: FlightOptionsList = field(
        default=None,
        metadata=dict(
            name="FlightOptionsList",
            type="Element",
            help=None,
        )
    )
    baggage_allowances: BaggageAllowances = field(
        default=None,
        metadata=dict(
            name="BaggageAllowances",
            type="Element",
            help=None,
        )
    )
    fare_rules_filter: FareRulesFilter = field(
        default=None,
        metadata=dict(
            name="FareRulesFilter",
            type="Element",
            help=None,
        )
    )
    policy_codes_list: PolicyCodesList = field(
        default=None,
        metadata=dict(
            name="PolicyCodesList",
            type="Element",
            help="A list of codes that indicate why an item was determined to be ‘out of policy’",
        )
    )
    price_change: List[PriceChangeType] = field(
        default_factory=list,
        metadata=dict(
            name="PriceChange",
            type="Element",
            help="Indicates a price change is found in Fare Control Manager",
            min_occurs=0,
            max_occurs=99
        )
    )
    action_details: ActionDetails = field(
        default=None,
        metadata=dict(
            name="ActionDetails",
            type="Element",
            help=None,
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            help="Allows an agency to update the commission to a new or different commission rate which will be applied at time of ticketing. The commission Modifier allows the user specify how the commission change is to applied",
            min_occurs=0,
            max_occurs=999
        )
    )
    origin: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Origin",
            type="Attribute",
            help="The IATA location code for this origination of this entity.",
        )
    )
    destination: TypeIatacode = field(
        default=None,
        metadata=dict(
            name="Destination",
            type="Attribute",
            help="The IATA location code for this destination of this entity.",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    command_key: str = field(
        default=None,
        metadata=dict(
            name="CommandKey",
            type="Attribute",
            help="The command identifier used when this is in response to an AirPricingCommand. Not used in any request processing.",
            max_length=10.0
        )
    )
    amount_type: StringLength1to32 = field(
        default=None,
        metadata=dict(
            name="AmountType",
            type="Attribute",
            help="This field displays type of payment amount when it is non-monetary. Presently available/supported value is 'Flight Pass Credits'.",
        )
    )
    includes_vat: bool = field(
        default=None,
        metadata=dict(
            name="IncludesVAT",
            type="Attribute",
            help="Indicates whether the Base Price includes VAT.",
        )
    )
    exchange_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ExchangeAmount",
            type="Attribute",
            help="The amount to pay to cover the exchange of the fare (includes penalties).",
        )
    )
    forfeit_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute",
            help="The amount forfeited when the fare is exchanged.",
        )
    )
    refundable: bool = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            help="Indicates whether the fare is refundable",
        )
    )
    exchangeable: bool = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute",
            help="Indicates whether the fare is exchangeable",
        )
    )
    latest_ticketing_time: str = field(
        default=None,
        metadata=dict(
            name="LatestTicketingTime",
            type="Attribute",
            help="The latest date/time at which this pricing information is valid",
        )
    )
    pricing_method: TypePricingMethod = field(
        default=None,
        metadata=dict(
            name="PricingMethod",
            type="Attribute",
            help=None,
            required=True
        )
    )
    checksum: str = field(
        default=None,
        metadata=dict(
            name="Checksum",
            type="Attribute",
            help="A security value used to guarantee that the pricing data sent in matches the pricing data previously returned",
        )
    )
    eticketability: TypeEticketability = field(
        default=None,
        metadata=dict(
            name="ETicketability",
            type="Attribute",
            help="The E-Ticketability of this AirPricing",
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="The Plating Carrier for this journey",
        )
    )
    provider_reservation_info_ref: TypeRef = field(
        default=None,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Attribute",
            help="Provider reservation reference key.",
        )
    )
    air_pricing_info_group: int = field(
        default=None,
        metadata=dict(
            name="AirPricingInfoGroup",
            type="Attribute",
            help="This attribute is added to support multiple store fare in Host. All AirPricingInfo with same group number will be stored together.",
        )
    )
    total_net_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="TotalNetPrice",
            type="Attribute",
            help="The total price of a negotiated fare.",
        )
    )
    ticketed: bool = field(
        default=None,
        metadata=dict(
            name="Ticketed",
            type="Attribute",
            help="Indicates if the associated stored fare is ticketed or not.",
        )
    )
    pricing_type: str = field(
        default=None,
        metadata=dict(
            name="PricingType",
            type="Attribute",
            help="Indicates the Pricing Type used. The possible values are TicketRecord, StoredFare, PricingInstruction.",
            max_length=25.0
        )
    )
    true_last_date_to_ticket: str = field(
        default=None,
        metadata=dict(
            name="TrueLastDateToTicket",
            type="Attribute",
            help="This date indicates the true last date/time to ticket for the fare. This date comes from the filed fare . There is no guarantee the fare will still be available on that date or that the fare amount may change. It is merely the last date to purchase a ticket based on the carriers fare rules at the time the itinerary was quoted and stored",
        )
    )
    fare_calculation_ind: str = field(
        default=None,
        metadata=dict(
            name="FareCalculationInd",
            type="Attribute",
            help="Fare calculation that was used to price the itinerary.",
            length=1
        )
    )
    cat35_indicator: bool = field(
        default=None,
        metadata=dict(
            name="Cat35Indicator",
            type="Attribute",
            help="A true value indicates that the fare has a Cat35 rule. A false valud indicates that the fare does not have a Cat35 rule",
        )
    )


@dataclass
class FareInfoList:
    """
    The shared object list of FareInfos
    """

    fare_info: List[FareInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FareInfo",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirExchangeMulitQuoteList:
    """
    The shared object list of AirExchangeMultiQuotes
    """

    air_exchange_multi_quote_option: List[AirExchangeMultiQuoteOption] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeMultiQuoteOption",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )


@dataclass
class AirPricePoint(AttrPrices):
    """
    The container which holds the Non Solutioned result.
    """

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingResultMessage",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help="Supported by ACH only",
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Itinerary level taxes",
            min_occurs=0,
            max_occurs=999
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    complete_itinerary: bool = field(
        default="true",
        metadata=dict(
            name="CompleteItinerary",
            type="Attribute",
            help="This attribute is used to return whether complete Itinerary is present in the AirPricePoint structure or not. If set to true means AirPricePoint contains the result for full requested itinerary.",
        )
    )


@dataclass
class AirPricingInfoList:
    """
    The shared object list of AirSegments
    """

    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPricingSolution(AttrPrices):
    """
    The pricing container for an air travel itinerary
    """

    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment_ref: List[AirSegmentRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegmentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    journey: List[Journey] = field(
        default_factory=list,
        metadata=dict(
            name="Journey",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    leg_ref: List[LegRef] = field(
        default_factory=list,
        metadata=dict(
            name="LegRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note_ref: List[FareNoteRef] = field(
        default_factory=list,
        metadata=dict(
            name="FareNoteRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    connection: List[Connection] = field(
        default_factory=list,
        metadata=dict(
            name="Connection",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    meta_data: List[MetaData] = field(
        default_factory=list,
        metadata=dict(
            name="MetaData",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_result_message: List[TypeResultMessage] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingResultMessage",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TaxInfo] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Itinerary level taxes",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_itinerary_solution_ref: List[AirItinerarySolutionRef] = field(
        default_factory=list,
        metadata=dict(
            name="AirItinerarySolutionRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    host_token: List[HostToken] = field(
        default_factory=list,
        metadata=dict(
            name="HostToken",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help=None,
        )
    )
    available_ssr: AvailableSsr = field(
        default=None,
        metadata=dict(
            name="AvailableSSR",
            type="Element",
            help=None,
        )
    )
    pricing_details: PricingDetails = field(
        default=None,
        metadata=dict(
            name="PricingDetails",
            type="Element",
            help=None,
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
            required=True
        )
    )
    complete_itinerary: bool = field(
        default="true",
        metadata=dict(
            name="CompleteItinerary",
            type="Attribute",
            help="This attribute is used to return whether complete Itinerary is present in the AirPricingSolution structure or not. If set to true means AirPricingSolution contains the result for full requested itinerary.",
        )
    )
    quote_date: str = field(
        default=None,
        metadata=dict(
            name="QuoteDate",
            type="Attribute",
            help="This date will be equal to the date of the transaction unless the request included a modified ticket date.",
        )
    )
    itinerary: str = field(
        default=None,
        metadata=dict(
            name="Itinerary",
            type="Attribute",
            help="For an exchange request this tells if the itinerary is the original one or new one. A value of Original will only apply to 1G/1V/1P/1S/1A. A value of New will apply to 1G/1V/1P/1S/1A/ACH.",
        )
    )


@dataclass
class Etr(AttrPrices, AttrElementKeyResults):
    """
    Result of ticketing request
    """

    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help=None,
        )
    )
    agency_info: AgencyInfo = field(
        default=None,
        metadata=dict(
            name="AgencyInfo",
            type="Element",
            help=None,
        )
    )
    booking_traveler: BookingTraveler = field(
        default=None,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            help=None,
            required=True
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            help="This is a container to display detail information of credit card auth. Providers supported: Worldspan and JAL.",
            min_occurs=0,
            max_occurs=999
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_calc: FareCalc = field(
        default=None,
        metadata=dict(
            name="FareCalc",
            type="Element",
            help=None,
            required=True
        )
    )
    ticket: List[Ticket] = field(
        default_factory=list,
        metadata=dict(
            name="Ticket",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    commission: List[Commission] = field(
        default_factory=list,
        metadata=dict(
            name="Commission",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: AirPricingInfo = field(
        default=None,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            help=None,
        )
    )
    audit_data: AuditData = field(
        default=None,
        metadata=dict(
            name="AuditData",
            type="Element",
            help=None,
        )
    )
    restriction: List[Restriction] = field(
        default_factory=list,
        metadata=dict(
            name="Restriction",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    waiver_code: WaiverCode = field(
        default=None,
        metadata=dict(
            name="WaiverCode",
            type="Element",
            help=None,
        )
    )
    baggage_allowances: BaggageAllowances = field(
        default=None,
        metadata=dict(
            name="BaggageAllowances",
            type="Element",
            help="Baggage Allowance Info after Ticketing",
        )
    )
    key: TypeRef = field(
        default=None,
        metadata=dict(
            name="Key",
            type="Attribute",
            help=None,
        )
    )
    refundable: bool = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            help=None,
        )
    )
    exchangeable: bool = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute",
            help=None,
        )
    )
    tour_code: TypeTourCode = field(
        default=None,
        metadata=dict(
            name="TourCode",
            type="Attribute",
            help=None,
        )
    )
    issued_date: str = field(
        default=None,
        metadata=dict(
            name="IssuedDate",
            type="Attribute",
            help="Ticket issue date.",
            required=True
        )
    )
    bulk_ticket: bool = field(
        default=None,
        metadata=dict(
            name="BulkTicket",
            type="Attribute",
            help="Whether the ticket was issued as bulk.",
        )
    )
    provider_code: TypeProviderCode = field(
        default=None,
        metadata=dict(
            name="ProviderCode",
            type="Attribute",
            help="Contains the Provider Code of the provider that houses this ETR.",
        )
    )
    provider_locator_code: TypeProviderLocatorCode = field(
        default=None,
        metadata=dict(
            name="ProviderLocatorCode",
            type="Attribute",
            help="Contains the Locator Code of the Provider Reservation that houses this ETR.",
        )
    )
    iatanumber: TypeIata = field(
        default=None,
        metadata=dict(
            name="IATANumber",
            type="Attribute",
            help="Contains the IATA Number of the agent initiating the request.",
        )
    )
    pseudo_city_code: TypePcc = field(
        default=None,
        metadata=dict(
            name="PseudoCityCode",
            type="Attribute",
            help="Contain Pseudo City, city/office number, branch ID, etc.",
        )
    )
    country_code: TypeCountry = field(
        default=None,
        metadata=dict(
            name="CountryCode",
            type="Attribute",
            help="Contains Ticketed PCC’s Country code.",
        )
    )
    plating_carrier: TypeCarrier = field(
        default=None,
        metadata=dict(
            name="PlatingCarrier",
            type="Attribute",
            help="Contains the Plating Carrier of this ETR.",
        )
    )


@dataclass
class Tcr(ProviderReservation):
    """
    Information related to Ticketless carriers
    """

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    booking_traveler: List[BookingTraveler] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTraveler",
            type="Element",
            help=None,
            min_occurs=1,
            max_occurs=999
        )
    )
    passenger_ticket_number: List[PassengerTicketNumber] = field(
        default_factory=list,
        metadata=dict(
            name="PassengerTicketNumber",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    agency_info: AgencyInfo = field(
        default=None,
        metadata=dict(
            name="AgencyInfo",
            type="Element",
            help=None,
        )
    )
    air_reservation_locator_code: AirReservationLocatorCode = field(
        default=None,
        metadata=dict(
            name="AirReservationLocatorCode",
            type="Element",
            help=None,
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    refund_remark: List[RefundRemark] = field(
        default_factory=list,
        metadata=dict(
            name="RefundRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tcrnumber: TypeTcrnumber = field(
        default=None,
        metadata=dict(
            name="TCRNumber",
            type="Attribute",
            help="The identifying number for a Ticketless Air Reservation.",
            required=True
        )
    )
    status: TypeTcrstatus = field(
        default=None,
        metadata=dict(
            name="Status",
            type="Attribute",
            help="The current status of this TCR. Some status values are not applicable by some Airlines.",
            required=True
        )
    )
    modified_date: str = field(
        default=None,
        metadata=dict(
            name="ModifiedDate",
            type="Attribute",
            help="The date at which the status was changed on this TCR due to an action event (itemized from the booleans below).",
            required=True
        )
    )
    confirmed_date: str = field(
        default=None,
        metadata=dict(
            name="ConfirmedDate",
            type="Attribute",
            help="The date at which this TCR was confirmed (not created). This mean the payment was approved and processed and travel for this TCR is confirmed.",
        )
    )
    base_price: TypeMoney = field(
        default=None,
        metadata=dict(
            name="BasePrice",
            type="Attribute",
            help="The base price of this TCR as a whole as it was when it was first booked.",
            required=True
        )
    )
    taxes: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Taxes",
            type="Attribute",
            help="The taxes of this TCR as a whole as it was when it was first booked.",
            required=True
        )
    )
    fees: TypeMoney = field(
        default=None,
        metadata=dict(
            name="Fees",
            type="Attribute",
            help="The fees of this TCR as a whole as it was when it was first booked.",
            required=True
        )
    )
    refundable: bool = field(
        default=None,
        metadata=dict(
            name="Refundable",
            type="Attribute",
            help="Is it possible to perform a Refund for this TCR.",
            required=True
        )
    )
    exchangeable: bool = field(
        default=None,
        metadata=dict(
            name="Exchangeable",
            type="Attribute",
            help="Is it possible to perform an Exchange for this TCR.",
            required=True
        )
    )
    voidable: bool = field(
        default=None,
        metadata=dict(
            name="Voidable",
            type="Attribute",
            help="Is it possible to perform a Void on this TCR.",
            required=True
        )
    )
    modifiable: bool = field(
        default=None,
        metadata=dict(
            name="Modifiable",
            type="Attribute",
            help="Is it possible to modify this TCR (opposed to Refund/Exchange/Void).",
            required=True
        )
    )
    refund_access_code: RefundAccessCode = field(
        default=None,
        metadata=dict(
            name="RefundAccessCode",
            type="Attribute",
            help=None,
        )
    )
    refund_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RefundAmount",
            type="Attribute",
            help="Total Amount refunded to the customer.",
        )
    )
    refund_fee: TypeMoney = field(
        default=None,
        metadata=dict(
            name="RefundFee",
            type="Attribute",
            help="Charges incurred for processing refund.",
        )
    )
    forfeit_amount: TypeMoney = field(
        default=None,
        metadata=dict(
            name="ForfeitAmount",
            type="Attribute",
            help="Amount forfeited as a result of refund.",
        )
    )


@dataclass
class TypeBaseAirReservation(BaseReservation):
    """
    Parent Container for Air Reservation
    """

    optional_services: OptionalServices = field(
        default=None,
        metadata=dict(
            name="OptionalServices",
            type="Element",
            help=None,
        )
    )
    supplier_locator: List[SupplierLocator] = field(
        default_factory=list,
        metadata=dict(
            name="SupplierLocator",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    third_party_information: List[ThirdPartyInformation] = field(
        default_factory=list,
        metadata=dict(
            name="ThirdPartyInformation",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    document_info: DocumentInfo = field(
        default=None,
        metadata=dict(
            name="DocumentInfo",
            type="Element",
            help=None,
        )
    )
    booking_traveler_ref: List[BookingTravelerRef] = field(
        default_factory=list,
        metadata=dict(
            name="BookingTravelerRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    provider_reservation_info_ref: List[ProviderReservationInfoRef] = field(
        default_factory=list,
        metadata=dict(
            name="ProviderReservationInfoRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_segment: List[AirSegment] = field(
        default_factory=list,
        metadata=dict(
            name="AirSegment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    svc_segment: List[SvcSegment] = field(
        default_factory=list,
        metadata=dict(
            name="SvcSegment",
            type="Element",
            help="Service segment added to collect additional fee. 1P only",
            min_occurs=0,
            max_occurs=999
        )
    )
    air_pricing_info: List[AirPricingInfo] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    payment: List[Payment] = field(
        default_factory=list,
        metadata=dict(
            name="Payment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    credit_card_auth: List[CreditCardAuth] = field(
        default_factory=list,
        metadata=dict(
            name="CreditCardAuth",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fare_note: List[FareNote] = field(
        default_factory=list,
        metadata=dict(
            name="FareNote",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    fee_info: List[FeeInfo] = field(
        default_factory=list,
        metadata=dict(
            name="FeeInfo",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    tax_info: List[TypeTaxInfoWithPaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="TaxInfo",
            type="Element",
            help="Itinerary level taxes",
            min_occurs=0,
            max_occurs=999
        )
    )
    ticketing_modifiers: List[TicketingModifiers] = field(
        default_factory=list,
        metadata=dict(
            name="TicketingModifiers",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    associated_remark: List[AssociatedRemark] = field(
        default_factory=list,
        metadata=dict(
            name="AssociatedRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    pocket_itinerary_remark: List[PocketItineraryRemark] = field(
        default_factory=list,
        metadata=dict(
            name="PocketItineraryRemark",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_exchange_bundle_total: AirExchangeBundleTotal = field(
        default=None,
        metadata=dict(
            name="AirExchangeBundleTotal",
            type="Element",
            help=None,
        )
    )
    air_exchange_bundle: List[AirExchangeBundle] = field(
        default_factory=list,
        metadata=dict(
            name="AirExchangeBundle",
            type="Element",
            help="Bundle exchange, pricing, and penalty information. Providers ACH/1G/1V/1P",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPricePointList:
    """
    Provides the list of AirPricePoint (Non Solutioned Result)
    """

    air_price_point: List[AirPricePoint] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricePoint",
            type="Element",
            help="The container which holds the Non Solutioned result. Different options for each search leg requested will be returned and one option for each search leg can be selected.",
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class AirPriceResult:
    """
    A solution will be returned if one exists. Otherwise an error will be present
    """

    air_pricing_solution: List[AirPricingSolution] = field(
        default_factory=list,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=99
        )
    )
    fare_rule: List[FareRule] = field(
        default_factory=list,
        metadata=dict(
            name="FareRule",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    air_price_error: TypeResultMessage = field(
        default=None,
        metadata=dict(
            name="AirPriceError",
            type="Element",
            help=None,
        )
    )
    command_key: str = field(
        default=None,
        metadata=dict(
            name="CommandKey",
            type="Attribute",
            help="The command identifier used when this is in response to an AirPricingCommand. Not used in any request processing.",
            max_length=10.0
        )
    )


@dataclass
class AirReservation(TypeBaseAirReservation):
    """
    The parent container for all booking data
    """

    pass


@dataclass
class AirScheduleChangedInfo:
    """
    Contents will be a new AirPricingSolution that contains all the new schedule information as well as the pricing information.
    """

    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            required=True
        )
    )


@dataclass
class AirSolutionChangedInfo:
    """
    If RetainReservation is None, this will contain the new values returned from the provider. If RetainReservation is Price, Schedule, or Both and there is a price/schedule change, this will contain the new values that were returned from the provider. If RetainReservation is Price, Schedule, or Both and there isn’t a price/schedule change, this element will not be returned.
    """

    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            required=True
        )
    )
    reason_code: str = field(
        default=None,
        metadata=dict(
            name="ReasonCode",
            type="Attribute",
            help=None,
            required=True
        )
    )


@dataclass
class OptionalServicesInfo:
    air_pricing_solution: AirPricingSolution = field(
        default=None,
        metadata=dict(
            name="AirPricingSolution",
            type="Element",
            help=None,
            required=True
        )
    )
    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )
    form_of_payment_ref: List[FormOfPaymentRef] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPaymentRef",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )


@dataclass
class TypeAirReservationWithFop(TypeBaseAirReservation):
    """
    Air Reservation With Form Of Payment.
    """

    form_of_payment: List[FormOfPayment] = field(
        default_factory=list,
        metadata=dict(
            name="FormOfPayment",
            type="Element",
            help=None,
            min_occurs=0,
            max_occurs=999
        )
    )