<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
xmlns:xs="http://www.w3.org/2001/XMLSchema"
version="1.0">
<xsl:output method="xml" version="1.0" encoding="UTF-8" />
    <xsl:template match="/">
    <html>
        <body>
            <h2>Jugadores del Equipo</h2>
            <table border="1">
                <tr bgcolor="#9acd32">
                    <th>Nombre</th>
                    <th>Nacionalidad</th>
                    <th>Posicion</th>
                    <th>Edad</th>
                  </tr>
                <Player>
                    <xsl:for-each select="XMLSOCCER.COM/Player">
                        <xsl:variable name="now" select="current-dateTime" />
                        <xsl:variable name="past" select="substring(DateOfBirth,1,4)"/>
                        
                        <Fichaje>
                            <Id>
                                <xsl:attribute name="Numero"><xsl:value-of select='Id'/></xsl:attribute> 
                            </Id>
                                <Datos>
                                    <tr>
                                        <td><Nombre><xsl:value-of select="Name"/></Nombre></td>
                                        <td><Nacionalidad><xsl:value-of select="Nationality"/></Nacionalidad></td>
                                        <td><Posicion><xsl:value-of select="Position"/></Posicion></td>
                                        <xsl:choose>
                                            <xsl:when test="DateOfBirth">
                                                <td><Edad><xsl:value-of select="2021 - $past"/></Edad></td>
                                            </xsl:when>
                                            <xsl:otherwise>
                                                <td><Edad>-</Edad></td>
                                            </xsl:otherwise>>
                                        </xsl:choose>
                                      </tr>                                    
                                </Datos>
                        </Fichaje>
                    </xsl:for-each>
                </Player>
            </table>
        </body>
    </html>          
    </xsl:template> 
</xsl:stylesheet> 
