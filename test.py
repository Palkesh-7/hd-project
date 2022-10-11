#  data1  = (BytesIO(base64.urlsafe_b64decode(data['img'])))
#         print(data1)

#         img2 = Image.open(data1)
#         now = datetime.datetime.now()
#         img_path2 = os.path.sep.join(['static/shot', "shot_{}.jpg".format(str(now).replace(":",''))])	
#         # img_path2 = "static/shot" + img2.filename	
#         img2.save(img_path2)
#         result2 = predict_label(img_path2)
#         return render_template("output.html", prediction=result2["class"],confidence = result2["confidence"],img_path = img_path2)


# import PIL.Image as Image 



import json
import base64
from codecs import encode

request = b'"{\\"image\\": \\"/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAoHCBYVFRgVEhUZGBgYGBoYGBkYGBgYGhgYGBgZGhgYGBgcIS4lHB4rIRgYJjgmKy8xNTU1GiQ7QDs0Py40NTEBDAwMEA8QGhISGDQhISM0MTQ0NDQ0NDQ0NDE2MTE0NDQ0NDQ0NDQ0NDE0NDQ0NDE0NDE0NDQ0NjQ0NDQxNDQxNP/AABEIAKIBNwMBIgACEQEDEQH/xAAcAAAABwEBAAAAAAAAAAAAAAAAAQIDBAUGBwj/xABCEAABAwEFBAcEBwcDBQAAAAABAAIRAwQSITFBBVFhcQYiMoGRsfATQqHBFFJygpLR4QcjM2KisvE0c7MVJENjwv/EABkBAAMBAQEAAAAAAAAAAAAAAAABAgMEBf/EACMRAQEBAQABBQACAwEAAAAAAAABAhExAxIhQVEEYTJxsRP/2gAMAwEAAhEDEQA/ANABinWpEYp1oQDbk28YhOFE4YhAOBLaEQCUEyFUEtMqsBk3TlorKsYaVWtgqaqDuFuWSepVAUGbim30YMhHkLGmAQVb0hDRCo7JVkxrK0VNuXJTo4epPkJ0BRXsumQpNJ0hOCjeMFEo1LpjRTHnBMMpghFEPvdIUfau0WWai+tUMNY2c4Ljo0cScEGOLTdK5n+0ba7q9oFmYepSPWA96oRiTyBgcylbw5O1WG1PtdZ1pr74Yz3WDQAcN+pUp7VJsVnApNwyTdoC59XtdeZJOIUqxsYOG5V78FPsNTLFK+GmVvTi9CvLJTCoab+tjuV1YKu9TPKtW8TmsT7Qm2CfXJTWWfCVrIw1rnllelmyL7PbUxFSn1hGbmjNvGMx371R2K0iowPGuY3EZhdCqM0K51a6H0a2PpgQyr1mbg7EwB3HwC6/4nqXOvbfF/65f5OJvPunmf8AExEjQhep154IIQhCZAEoBFCUEjKCy9v/AIhWpAWYtjf3hU6qbO/CBUspc5PixkxwTntw1Iq2wiI1WdvTkzInBsCESIGQCgk0bNgTgCSwJxcLqMQg4YhLhE4ZIIoJRRBGUAmsJYVUNaWlW9TsqK1gKVpwhr5S7+hTb6RGISWGcClw02x0RfaVpqYxVFs1nWEq+pJU4dc2QmILTwUkFJc2RikYOdIRURgozyW4aKRQyQCLc8NY559xpd4CVxClUL6jqju09xcebiSuv9LLRcslYzEsLRG9/V+a4/ZmwcN+Cja8NJY3QyCmq6fszCGhMWkwsnTEOq2FPsLRLRvx9fFV73ypuzyS5g3HPnglfCpWks9Ge8KVZwJiMs8EmzVWhjATi4uA+6JKVYCHmRjilFdXdkoyJ3qws5IwPrkVHotujEwpF6Fvn4cm703am6rG9ObJeptqN7bDIPeCPiFr67lnekLuoR63o7y9iszs5VBQqB7WuHvAHxTiYsTYYBukd0mE+vaze5l/XlanLZ+AgjQVJBKCSlNQCll7a/rkLUrKWv8AiOU1Ou8+ER4Epu1e7zCmsoAmSnXUm6qNUs4v2XT7IQS9MEalq2jAlkYJLAluyXC6yAieMkoBB4xQQgiclAJLwgG7S+Gpmi6UNpyGYKDY6shKnFqQmKlHUJTKkp4JGkbIJLsdFdUnwcVW7KZiSrG5Km+VTwlSjhRqNTQqUiAzWZITVJ8GE/VyQFIEICg6du/7J+ObmD+sLm+y6N54nTFX/SbbDrSatnpu6jHwRdGNx0Xg7PMEd6qNiUiHun3RE8ystalb4xc86uK9QMbOpyWft9dwxMAc1Z7UqGRdEnQeSzlt2O9wL6rr5cOq2YDDP9SjMaU03bADsSCN8hWNHbI9zx/wqClsxjGm9MndECOOqFhsjr40E4j58FesxObXQNjbQFSrSaAQymxwx1JxcfgPBMdHtqXC4vOB9QrnobshrgXvAIiI4AYrGdJ6brNWexohsy29lByxWXtv0190nxXVbFtilUaOu2dxwxhWFmqB2IOC89u2jVY7DygfBbropt9xeKVUuY8xdnIzuWnbPLP2zXZHSqpWQ6XVy0d3+AtJZqxcCHZhY7pw+XsaNBijyXOEWQyxp3tB8U8k0mQ0DcAEte5iczJ+PI3e6tEgjQVJAJTUSUEAZWWtY67jxWqOSyVq/iO5pX5LV58o7qzsgjcSYkoiMcE57M4KLJETWtJk4BBCMAgpbN0wJTkYag5cDrJAROzSgiOaYAIOCNmSWQglTt2sWU5CqrJXDus3PUK/2pQD2XSFkbRQfRdI7KOBo6cOEjNPUX6FU9jtd4S3A6hWlnqB/NI2h2UOqSrCkFB2W2GKwpZKFkVac5I6L9DmnE3Vp6jNAKqnAJ+looDXyQNynsdggONWYhnWces98kZkgyB5yp2yxIe7UvI7hgPJV1nd13Fwg4xw3x3SpuyXgX2/zuP9S5uO3VLtAglQq75zxUy0vkmFDfT3qsnxBdZ7xygb1Ns1iazEDv3lMmoG92m8q0cYBvbkWjjYdEiW04OsxyKHSbo8LSwFkCoyYnJw+q75HTvTPQyuHNiRIn4LSPqBsTqYniRgnnx8s92zXw5dYNnOY8e0oNJa6JutMEFa62dHWWpoc9rmVGjq1MnNOYN0RPeprqbXVL2Tp60e9G8eCubKZRM98q3rklk5VZYaL2tb7TtgAOIEAkarI7Wsrq1pcWtJAfBw0YBgMN4HxW+tLsVSWmu6lZ6tSnAN95BiesX3Rn3KpZiy+eI5d/HjvwoXNIMEQRmCiT1oeXBjnYucxpcd5xEnjACaXsenr3Zl/Y8n1MezWs/l4JGggtEDCUEkJQQBnJZO0j947mtYcispa6gD3Ab1NK8+ymFozRvtLQqiu4zmlvyap4Pf+Rcl0hEksyHJBS0dGqUSE09qv61mBCrbTZSF57r4gNCSnrqbcM0yEwYJ5jJTbBgptCnkihDtjIAVXabM1wIzBWstFlDmqitNkLOSJRYxdtsbqLr7Oz5Kbs+1h+LcHeatqzAeqQqC17NfTN+nN0GSBonSjf7OrdQA5qypFZDY9v8AagQYcB4rQWO1Y3XYFZtFnCNJa6UpBI1RkOwTtCrvSanaRvpahBuc7bsLqdZzBhdMgkZtcSQfAx3FU1IkEnST56ldI6Tln0dz3sBe2AwnMScYPKVzIZYbzhzOJy46rG55XRNdkSG1JMTPgjtDlGs9UT6z4JNoq6DEpLmjRmZGhnvCh1hVvlwc597C5p4HVPvr6epTuzWOc+YJABOXwT4Pd3wsdh1rTTe40mXnjAsc4NExgCZx5Baelb7W6zl1qYGvDwWkC7gJmBJMZCVTdHGOBe8tJ608IyWvpW1rhdcLwiOHJZql55iHsq1l5F7Pfj61Wne8Abis9ZLHceS3LTlx4q1rukGdPWSrNshepzVnAq2jAu3ZcToPW9VttpF1OpZ703XU4PN7HGTzJSKlSX02DIODnQM7pmY3YBPbRa2kx5aSXVdTu1Prerxm71Mz7T756c91+vmKW0OBd1eyIa3k0QD3xPem0aNe3nMzJJ9PH1q61dXzSUYQQVJGEoJISggDOR5LH2r+I7mtgcjyWSrs67jxU28KzvwiGylxlSBZMuCM2prUZtJwjVRbafMyJNyAiQB3oJLdrhNVKYKfCJwXnuxV17JhIVTUZErU3cFWWqy4EoJUNarGg3AJh9nIhTKDckBLTb6YcMQnXIkGzm0dmkOvNCaszARdcM1pXAFRHWIXw4I6XGT23sF9IitZsNXNGvEJ7Zu0hWABMPC2FSmDgsnt7YBDva0MHDEtGv6qeKXdjtfuuzVkx0rG7L2iKguP6r278MVe2O1kG67PzR0LI9pSGqNSMmVKATgZbp4+KLW/WLj+Fv6rnjQIPqPXyWy6abTove2k17S5l9rhOTiQC2ci4XcVjHYEDLLPfr+Xesdf5Vtn/GI7MDjEkmI9YJu3GIxj1jKU94DhMZ4BRtoPkxh8wlDNCo8dll7jon7ALQ937tpkbnNGu4nHGFKsr2gYJ+laC1wLcI4Ita55F1StFsZ1hRc7CHAXHB2/AGUunt9gj2jXU3/VIInkCpuwtquc64+64bwBB9Y+C0lpstOqwse1hBG4YEZHmFnzq9an4rrBa78EEHQEHeDmpNeocAXS6BllpoPWaz2xKJp1KjccHYboxy4a9yuXA48sOJjhronKyJNrNOoCADDCM8MYxHGJUS1Whz3XncgNANyK0Ol53CAOIAz+J8E2vW/jelnOZrnzXnev6t1q5+oJGggupzCRwggmBhGESUEgDsjyWQtLjfdzWvdkeSyFbtu5lJOu/SrtHaKl0zg1PssgJkp76OPBRaJi8+TgQRkQgpau2BAoBGVwOwQCaqNwUhNPCAafRBhMtpQVMhEQgI7wialVM0iEABmjATT7Qxn8R7G/ae1vmUdC0Mf2Htf9hzXeRQC3DEJTmSiGacUmym3tgXj7Sl1XjHnzULZ+0L/Uq9V7cMVotsbcstnJ+kV6bCB2S6X9zGy4+Cw21+lmz6suZUe17RLT7J4v8Bh5wjgbiwVogOz81jOl/wC0B9Or7OxOZDDD3loffeM2tnC6MpzJ1EY5LbHTmq+n7KlLGkQ5/wD5HDdI7I5Y8Vj/AGxTkC3/AOqF5iqZJ984yT9ffzzGm5WbbfeAa7tt1ntAjtTrh458ss4yEulaDF12QyOreI3jeEtZlVNcaWqRMg/FQa78cT5HLio9kt0dWprk4fDmOKl1YPeAd8mf8qOcV3qTZnTqryy7NvtwdA/xOHes1SeW+GnNXuy9q3BA7lOp+NM39aPZ2zbgvhxMYEREQrU2ohoLBI4g7sfJUWytqA4fWOpxJOXdxU2rWu4MwbHViYwiG9+IlZ8XdI1kquvk3ocSRvnLCdMoVjarSWw3MkwBOc5/DFVHtS0l93DSMSToN84+fFTqNNxN+p2jkPqjdOp4rf8Aj+jd6/r7Yer6sxn+y2NgAZxrv4o4S0lexI80SJKRJgSCNBCQSwkhKCQB+R5LJ1Wddx4rWvyPJY6pN93Mpa8AzUtd3AJL65w4qPaGkuKce3sqUdt6tZwCCLQIJNnbQjKAQK892FJt6cSHZoA0lLKxPTzpWbM32FBw9s5sudn7JhyP2jpuGO6QFdLOmNOykspgVK2rZ6jPtuGv8ox3wuZbV6U2quT7Su8NPuMNxkbrrYvD7RJVTVqEySZJJJJzJOZJ1UZ70AouEzAnHGBOPFKp1rpvNwcAAHDAjkRiFGe/5ph1X5INvNl9NLXTge2L2zdAqBr4AA989c56u0SrV0ltdWb1ofdPusu0xy6jQSOZKwlG2XT96fFXFhtQIbjo75lLgiTdPjiY3nem6+y2PGV07x8xkVYU2hwB5evNOsYkbD22yvpuuP5tOjm7wot5bnatgFRhES5vWZ9oaTuOXes3tLY5Y1tWn1qbgCDqzDFr90HCU5S4rGPRv3jNJLSjVAtlSRw1H1eI3t4f5TzLS4YHEaHnqN4UUNIMj5J0ZZYZkfV4t4cP0KVglTadryj13KSyuTv+Sqm0C4wBJOUa8loNn7AqlsvMDEgTLiBmYGcYSM9cQp1JF5tOWG1FpwdG+RMb4GpV3YbXUqdSm0vOGIBDQOJzG5L2L0dYXBz3B4OW7DeFt7NZmMDWU2hrcJjALHWp9NJKrbJs0UmBz4dUfiTo0bm/nzTxUm2ul0bhCjFer/Gz7cT+/l5/r692r/XwSUECgt2RKCCCACCCUgCCUEQSggCfkeSxz+27mVs6nZPJY2q4XnRvKnXhP2UymMyl3W8FW1KzpIlB7j1cVMyPfPqLYlBNzgEaS3bwgUAguB2FJDs0tN6oCB0g2uyy0HVn4xg1urnnst8czoAVwC22p9R7n1HXnvcXPdvcc+Q3DQADRbX9pu3xVrCgx0sok3o96qRB/COrzLlz6o/13KRwHOUd/wAkbqnyTT6vkfNUZDh5hINInQ6p42k/EfokNtBHh80AybM+MtAdO5BrXsMwRiRwUynaJ8W/NS6b5j7RPwCAlbH2jMA5wZ/EStCGSJCzVmswMEYdV0x9orQbPgNu8B5KTPsCiV7O9pL6Dg1xxex2LKmnWGjv5h3ypTuHr180CUBnPodnruugGzVtabgCxx/k/TwSH9FqwyLCBreI+BCta1lp13mlUF0t6zTk4t+sxw0BwO7UK1bSDWhoc5wAjrEuOG86p22D/bGv2I9hAqOaAcJEux3Ywptbo+AwupvLnjFuAAMZgDfH5arQ2yz327yPiPzUKzVC0wfH18Uu0cjLWOpdMjLMgZt/mbOm8foVr9m2uQATuOBzjJ7CciPzBVBtyxXHiozBjzOHuv1HI5+KOwWiIABgnFozafrsnTePHQos78nLxvdnV2B4vwJxvAYGPe3iNRm3ktW1jWNL3EQAXFxiIGMyFxy2bTe54pgG7O8sLnDJ4JyA3EY6zktDX6V1a1nfZ6gAq3gC+LjnNZiQ5mQcbumBxwEgKP8Az+etJv6a15kknXFIKgbCtoq0xvaACOGkcNPBWBC9bFlzLHmblmrKQiSikqyBJSkUIA0EUI0AAlhJCWEAVTsnksaacvdzPmtnU7J5LGF3WdzPmo14T9oFambxgJdSmergpzSEq+0Jdo9kHoEaUXIklu2o0AhquB2FFUvSfan0azVaw7TW3WfbeQ1ncCZ5Aq6K5n+1Xag/d2dp/wDa/wCLGD+8/hStEcxr1JJvEknMnEknMnjMqK+PXNSnmUy9vruShozmDFIcweakPb67k2Tw3KgaucNybcPJSPaYeJ8cE4WtdhGjR3nPyQCaNln8TfmpNOllwcfCEdEQcPr/AAbdP5p+lkPvHzCDHZ3kRP1XeF4qxs1WMQcmtPeIUBow+5PiRHmn6YInk0d8KQvncOPw9FER69esE1RcS08CSO7MeCWXiPXMfBBmLZZg8ZlrmmWPHaY7ePyyKcsFrLiWVAG1G4kDJ40ezgd2h7ktjvXrh5Jm12W/Dmm69hljs4OoO9pyI/JBLCFEtdmnrDv/ADSrDa77TeF17TD2zN07wdWnMFS2oNUhgex1OpkRG+DmCPNUj9n1GSxrXXsLzxIADphjXaggEk65b1oLXRumR64KfYKgeLp3gyeF4R/UU+iT5YuzWN94sIlxDozJ6oPZnvHPdmnzk0OmQcO1MxjIIgESDhrgtXadngVg9pghgBHA1HmfxBviqbbbSHsN0CWvvEakVCPGCPgiVXE/oxVcx5nI5+Ja6fC991bEhclt20HMe32T4LLxJaZBc+C5p0c0QMDqSuj9G9pfSbOx5EOEseP5m6jmIPeuz0Oycrl9blvYsCEUJwhIIXS5yUEaCAJCEEaAASwkhLAUgmqOqeSxdR/WcBvK2tXsnksUHC87mfNLXgqiiSTinQMklrCSU5cMhLsZc18pc4IIpwQSbu3hAIILgdhS4n+0f/XVeTP+JqCCnRxkBmif68EEEQzVT14KM/NBBBGxl935p9mf3x5lEgqCTY8x9/yKmUtPsu/uKCCkz7cj9hvk1StXfaCCCDTbB2u8/wBoTVDId3mgggHaeY9ap/Tu+QQQQSEP9TT40nzxg6q1YjQTohq19nuUWx5+tyCCRrK29tv+0P8AnYqbpDmzv/8AhBBE8rrEN0XSv2f/AOmd/uv/ALWIILux5cO/DTFJKCC2ZCRIIKgCCCCAUEYQQUiBV7J5LCntO5lBBTrwL5SaacGaCCmKByCCCYf/2Q==\\", \\"id\\": \\"e3ad9809-b84c-57f1-bd03-a54e25c59bcc\\"}"'

data_as_dictionary = json.loads(json.loads(request.decode('utf-8')))
base64_img = data_as_dictionary['image']
bytes_img = encode(base64_img, 'utf-8')
binary_img = base64.decodebytes(bytes_img)

with open("imageToSave.jpg", "wb") as fh:
   fh.write(binary_img)