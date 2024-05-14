from django.utils import timezone
from rest_framework import serializers
from ..models.masters import (
    Commodity,
    Country,
    State,
    Group,
    Parameter,
    Standard,
    Company,
    Branch,
    Lab,
    Roles,
    Mode,
    Entity,
    EntityHistory,
    EntityRolesRights,
    CommodityGroup,
    TenantMaster,
    Basis,
    CommoditySpecs
    
)


class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = "__all__"


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = "__all__"


class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    def validate(self, data):
        field_exp = ["<", ">", "%", "="]

        fields_to_validate = [
            "cmp_address",
            "cmp_phoneno",
            "cmp_pan_no",
            "cmp_cin_no",
            "cmp_gst_no",
            "cmp_iec_no",
        ]

        for field in fields_to_validate:
            if field in data and any(c in data[field] for c in field_exp):
                raise serializers.ValidationError(
                    f"The characters > % = < are not allowed in {field}."
                )
        return data

    def create(self, validated_data):
        validated_data["cmp_created_time"] = timezone.now()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["cmp_updated_time"] = timezone.now()
        return super().update(instance, validated_data)

    class Meta:
        model = Company
        fields = [
            "cmp_id",
            "cmp_name",
            "cmp_code",
            "cmp_address",
            "cmp_email",
            "cmp_state",
            "cmp_country",
            "cmp_phoneno",
            "cmp_pan_no",
            "cmp_cin_no",
            "cmp_gst_no",
            "cmp_iec_no",
            "cmp_created_time",
            "cmp_updated_time",
        ]
        extra_kwargs = {
            "cmp_id": {"read_only": True},
            "cmp_created_time": {"read_only": True},
            "cmp_updated_time": {"read_only": True},
        }


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = "__all__"


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class ModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mode
        fields = "__all__"


class EntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entity
        fields = "__all__"


class EntityHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityHistory
        fields = "__all__"


class EntityRolesRightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityRolesRights
        fields = "__all__"

class CommodityGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityGroup
        fields = "__all__"

class TenantMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantMaster
        fields = "__all__"

class BasisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basis
        fields = "__all__"

class CommoditySpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommoditySpecs
        fields = "__all__"
