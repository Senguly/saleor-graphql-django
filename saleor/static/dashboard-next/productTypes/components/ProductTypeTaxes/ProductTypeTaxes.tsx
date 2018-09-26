import Card from "@material-ui/core/Card";
import CardContent from "@material-ui/core/CardContent";
import * as React from "react";

import CardTitle from "../../../components/CardTitle";
import { ControlledCheckbox } from "../../../components/ControlledCheckbox";
import { FormSpacer } from "../../../components/FormSpacer";
import SingleSelectField from "../../../components/SingleSelectField";
import i18n from "../../../i18n";
import { translatedTaxRates as taxRates } from "../../../misc";
import { TaxRateType } from "../../../types/globalTypes";

interface ProductTypeTaxesProps {
  data: {
    chargeTaxes: boolean;
    taxRate: TaxRateType | null;
  };
  disabled: boolean;
  onChange: (event: React.ChangeEvent<any>) => void;
}
const taxRateChoices = Object.keys(taxRates()).map(key => ({
  label: taxRates()[key],
  value: key
}));
const ProductTypeTaxes: React.StatelessComponent<ProductTypeTaxesProps> = ({
  data,
  disabled,
  onChange
}) => (
  <Card>
    <CardTitle title={i18n.t("Shipping")} />
    <CardContent>
      <ControlledCheckbox
        checked={data.chargeTaxes}
        disabled={disabled}
        label={i18n.t("Charge taxes for this product")}
        name="chargeTaxes"
        onChange={onChange}
      />
      {data.chargeTaxes && (
        <>
          <FormSpacer />
          <SingleSelectField
            choices={taxRateChoices}
            label={i18n.t("Tax rate (optional)", {
              context: "select field label"
            })}
            name="taxRate"
            onChange={onChange}
            value={data.taxRate}
          />
        </>
      )}
    </CardContent>
  </Card>
);
ProductTypeTaxes.displayName = "ProductTypeTaxes";
export default ProductTypeTaxes;
