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
    EntityRolesRights,
    CommodityGroup,
    TenantMaster,
    Basis,
    CommoditySpecs,
)
from ..serializers.masterSerializers import (
    CommoditySerializer,
    CountrySerializer,
    StateSerializer,
    GroupSerializer,
    ParameterSerializer,
    StandardSerializer,
    CompanySerializer,
    BranchSerializer,
    LabSerializer,
    RolesSerializer,
    ModeSerializer,
    EntitySerializer,
    EntityRolesRightsSerializer,
    CommodityGroupSerializer,
    TenantMasterSerializer,
    BasisSerializer,
    CommoditySpecsSerializer,
)
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from master_api.error_messages import INVALID_ENTITY, messages

models = {
    "commodity": (Commodity, CommoditySerializer),
    "country": (Country, CountrySerializer),
    "state": (State, StateSerializer),
    "group": (Group, GroupSerializer),
    "parameter": (Parameter, ParameterSerializer),
    "standard": (Standard, StandardSerializer),
    "company": (Company, CompanySerializer),
    "branch": (Branch, BranchSerializer),
    "lab": (Lab, LabSerializer),
    "roles": (Roles, RolesSerializer),
    "mode": (Mode, ModeSerializer),
    "entity": (Entity, EntitySerializer),
    "entity_roles_rights": (EntityRolesRights, EntityRolesRightsSerializer),
    "commodity_group": (CommodityGroup, CommodityGroupSerializer),
    "tenant_master": (TenantMaster, TenantMasterSerializer),
    "basis": (Basis, BasisSerializer),
    "commodity_specs": (CommoditySpecs, CommoditySpecsSerializer),
}


class MasterCreateViewSet(viewsets.ViewSet):
    """
    A viewset for creating new instances of models.

    Supported models:
    - Commodity
    - Country
    - State
    - Group
    - Parameter
    - Standard
    - Company
    - Branch
    - Lab
    - Roles
    - Mode
    - Entity
    - EntityRolesRights
    - CommodityGroup
    - TenantMaster
    - Basis
    - CommoditySpecs
    """

    def create(self, request):
        """
        Create a new instance of a model.

        Parameters:
        - model_name (str): The name of the model to create an instance of.
        - data (dict or list): The data to create the instance(s) with.

        Returns:
        - Response: The response containing the status, message, and data.
        """
        model_name = request.data.get("model_name")
        data = request.data.get("data")

        if model_name not in models:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": INVALID_ENTITY,
                    "data": [],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        model_class, serializer_class = models[model_name]

        if isinstance(data, list):
            # Create multiple Mode records
            serializer = serializer_class(data=data, many=True)
        else:
            # Create a single Mode record
            serializer = serializer_class(data=data)

        if serializer.is_valid():
            try:
                serializer.save()
                created = messages["create"].get(model_name)

                return Response(
                    {
                        "status": status.HTTP_201_CREATED,
                        "message": created,
                        "data": serializer.data,
                    }
                )
            except serializer.errors as e:
                no_created = messages["not_created"].get(model_name)

                return Response(
                    {
                        "status": status.HTTP_400_BAD_REQUEST,
                        "message": no_created,
                        "data": e,
                    }
                )
        error_messages = human_readable_errors(serializer)
        return Response(
            {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": error_messages,
                "data": [],
            },
            status=status.HTTP_400_BAD_REQUEST,
        )


class MasterUpdateViewSet(viewsets.ViewSet):
    """
    A viewset for updating instances of models.

    Supported models:
    - Commodity
    - Country
    - State
    - Group
    - Parameter
    - Standard
    - Company
    - Branch
    - Lab
    - Roles
    - Mode
    - Entity
    - EntityRolesRights
    - CommodityGroup
    - TenantMaster
    - Basis
    - CommoditySpecs
    """

    def update(self, request):
        """
        Update an instance of a model.

        Parameters:
        - model_name (str): The name of the model to update an instance of.
        - id (int): The ID of the instance to update.
        - data (dict): The data to update the instance with.

        Returns:
        - Response: The response containing the status, message, and data.
        """
        model_name = request.data.get("model_name")
        id = request.data.get("id")
        data = request.data.get("data")

        not_found = messages["not_found"].get(model_name)

        if model_name not in models:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": INVALID_ENTITY,
                    "data": [],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        model_class, serializer_class = models[model_name]
        if id is not None:
            try:
                instance = model_class.objects.get(pk=id)
            except model_class.DoesNotExist:
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": not_found,
                        "data": [],
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = serializer_class(instance, data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                update = messages["update"].get(model_name)
                return Response(
                    {
                        "status": status.HTTP_200_OK,
                        "message": update,
                        "data": serializer.data,
                    }
                )
            error_messages = human_readable_errors(serializer)
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": error_messages,
                    "data": [],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": not_found,
                    "data": [],
                },
                status=status.HTTP_404_NOT_FOUND,
            )


class MasterDeleteViewSet(viewsets.ViewSet):
    """
    A viewset for deleting instances of models.

    Supported models:
    - Commodity
    - Country
    - State
    - Group
    - Parameter
    - Standard
    - Company
    - Branch
    - Lab
    - Roles
    - Mode
    - Entity
    - EntityRolesRights
    - CommodityGroup
    - TenantMaster
    - Basis
    - CommoditySpecs
    """

    def delete(self, request):
        """
        Delete an instance of a model.

        Parameters:
        - model_name (str): The name of the model to delete an instance of.
        - id (int): The ID of the instance to delete.

        Returns:
        - Response: The response containing the status, message, and data.
        """
        model_name = request.data.get("model_name")
        if model_name not in models:
            return Response(
                {INVALID_ENTITY},
                status=status.HTTP_400_BAD_REQUEST,
            )

        (model_class,) = models[model_name]
        try:
            instance = model_class.objects.get(pk=request.data.get("id"))
        except model_class.DoesNotExist:
            not_found = messages["not_found"].get(model_name)
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": not_found,
                    "data": [],
                }
            )
        instance.delete()
        delete = messages["delete"].get(model_name)
        return Response(
            {
                "status": status.HTTP_204_NO_CONTENT,
                "message": delete,
            },
            status=status.HTTP_204_NO_CONTENT,
        )


class MasterListViewSet(viewsets.ViewSet):
    """
    A viewset for listing instances of models.

    Supported models:
    - Commodity
    - Country
    - State
    - Group
    - Parameter
    - Standard
    - Company
    - Branch
    - Lab
    - Roles
    - Mode
    - Entity
    - EntityRolesRights
    - CommodityGroup
    - TenantMaster
    - Basis
    - CommoditySpecs
    """

    def list(self, request):
        """
        List instances of a model.

        Parameters:
        - model_name (str): The name of the model to list instances of.

        Returns:
        - Response: The response containing the status, message, and data.
        """
        model_name = request.data.get("model_name")
        if model_name not in models:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": INVALID_ENTITY,
                    "data": [],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        model_class, serializer_class = models[model_name]
        try:
            instance = model_class.objects.all()
        except model_class.DoesNotExist:
            not_found = messages["not_found"].get(model_name)
            return Response(
                {
                    "status": status.HTTP_404_NOT_FOUND,
                    "message": not_found,
                    "data": [],
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = serializer_class(instance, many=True)
        fetch = messages["fetch"].get(model_name)
        return Response(
            {
                "status": status.HTTP_200_OK,
                "message": fetch,
                "data": serializer.data,
            }
        )


class MasterRetrieveViewSet(viewsets.ViewSet):
    """
    A viewset for retrieving instances of models.

    Supported models:
    - Commodity
    - Country
    - State
    - Group
    - Parameter
    - Standard
    - Company
    - Branch
    - Lab
    - Roles
    - Mode
    - Entity
    - EntityRolesRights
    - CommodityGroup
    - TenantMaster
    - Basis
    - CommoditySpecs
    """

    def retrieve(self, request):
        """
        Retrieve an instance of a model.

        Parameters:
        - id (int): The ID of the instance to retrieve.
        - model_name (str): The name of the model to retrieve an instance of.

        Returns:
        - Response: The response containing the status, message, and data.
        """
        id = request.data.get("id")
        model_name = request.data.get("model_name")
        if model_name not in models:
            return Response(
                {
                    "status": status.HTTP_400_BAD_REQUEST,
                    "message": INVALID_ENTITY,
                    "data": [],
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        model_class, serializer_class = models[model_name]
        if id and model_name:
            try:
                instance = model_class.objects.get(pk=id)
            except model_class.DoesNotExist:
                not_found = messages["not_found"].get(model_name)
                return Response(
                    {
                        "status": status.HTTP_404_NOT_FOUND,
                        "message": not_found,
                        "data": [],
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
            serializer = serializer_class(instance)
            fetch = messages["fetch"].get(model_name)
            return Response(
                {
                    "status": status.HTTP_200_OK,
                    "message": fetch,
                    "data": serializer.data,
                }
            )


def human_readable_errors(serializer):
    """
    Convert serializer errors to human-readable format.

    Parameters:
    - serializer (Serializer): The serializer containing the errors.

    Returns:
    - list: The list of human-readable error messages.
    """
    errors = dict(serializer.errors)
    human_readable_errors = []

    for field, error_messages in errors.items():
        for error_message in error_messages:

            human_readable_errors.append(f"{error_message}")

    return " ".join(human_readable_errors)
